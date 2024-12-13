from django.db import models
from django.utils.timezone import now

class Player(models.Model):
    id = models.AutoField(primary_key=True)  # Auto-incremented ID
    username = models.CharField(max_length=150, unique=True)  # Player's username, must be unique
    email = models.EmailField(unique=True)  # Player's email, must be unique
    total_matches = models.IntegerField(default=0)  # Total matches played
    win_rate = models.FloatField(default=0.0)  # Win rate as a percentage
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)  # Profile picture
    created_at = models.DateTimeField(default=now)  # Timestamp when the player is created

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Player"
        verbose_name_plural = "Players"
        ordering = ['-created_at']  # Order by newest players first
