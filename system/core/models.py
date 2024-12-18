from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.text import slugify
from django.core.exceptions import ValidationError
from datetime import timedelta

class Player(models.Model):
    playerID = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Hashed password
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    games = models.ManyToManyField('Game', related_name='players')
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.pk or Player.objects.filter(pk=self.pk).exists():
            self.password = make_password(self.password) # type: ignore
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username


class Game(models.Model):
    game_id = models.AutoField(primary_key=True)
    game_name = models.CharField(max_length=100, unique=True, default='Unnamed Game')
    game_type = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.game_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.game_name


class Hero(models.Model):
    game = models.ForeignKey(Game, related_name='heroes', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    level = models.IntegerField(default=1)
    health = models.IntegerField(default=100)
    attack = models.IntegerField(default=10)
    defense = models.IntegerField(default=5)
    image = models.ImageField(upload_to='hero_images/', null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Hero"
        verbose_name_plural = "Heroes"
        unique_together = ('game', 'slug')


class Match(models.Model):
    game = models.ForeignKey(Game, related_name='matches', on_delete=models.CASCADE)
    hero_1 = models.ForeignKey(Hero, related_name='matches_as_hero_1', on_delete=models.CASCADE)
    hero_2 = models.ForeignKey(Hero, related_name='matches_as_hero_2', on_delete=models.CASCADE)
    winner = models.ForeignKey(Hero, related_name='won_matches', on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    duration = models.DurationField(null=True, blank=True)
    result = models.CharField(max_length=200, blank=True, null=True)

    def clean(self):
        if self.hero_1 == self.hero_2:
            raise ValidationError("A hero cannot match against itself.")

    def __str__(self):
        return f"Match between {self.hero_1.name} and {self.hero_2.name}"
