from django.db import models
from django.utils.timezone import now
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

# Create your models here.
from django.db import models
from django.contrib.auth.hashers import make_password

class Player(models.Model):
    playerID = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)  # Ensure unique usernames
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Use enough space for hashed passwords
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def save(self, *args, **kwargs):
        # Hash the password if it's not already hashed
        if not self.password.startswith('pbkdf2_sha256$'):  # Avoid re-hashing an already hashed password
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username

class Game(models.Model):
    game_id = models.AutoField(primary_key=True)
    game_name = models.CharField(max_length=100, unique=True, default='Unnamed Game')  # Set default here
    game_type = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)
    
    def __str__(self):
        return self.game_name


class Hero(models.Model):
    game = models.ForeignKey(Game, related_name='heroes', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    level = models.IntegerField(default=1)
    health = models.IntegerField(default=100)
    attack = models.IntegerField(default=10)
    defense = models.IntegerField(default=5)
    image = models.ImageField(upload_to='hero_images/', null=True, blank=True)  # Add image field
    slug = models.SlugField(unique=True, blank=True)
    
    def __str__(self):
        return self.name

class Match(models.Model):
    game = models.ForeignKey(Game, related_name='matches', on_delete=models.CASCADE)
    hero_1 = models.ForeignKey(Hero, related_name='matches_as_hero_1', on_delete=models.CASCADE)
    hero_2 = models.ForeignKey(Hero, related_name='matches_as_hero_2', on_delete=models.CASCADE)
    winner = models.ForeignKey(Hero, related_name='won_matches', on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    duration = models.DurationField(null=True, blank=True)  # Duration of the match, if relevant
    result = models.CharField(max_length=200, blank=True, null=True)  # Store a more detailed result

    def __str__(self):
        return f"Match between {self.hero_1.name} and {self.hero_2.name}"

