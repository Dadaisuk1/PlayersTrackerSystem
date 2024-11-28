from django.db import models

# Create your models here.

class Game(models.Model):
    game_id = models.AutoField(primary_key=True)
    game_name = models.CharField(max_length=100)
    game_type = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', blank=True, null=True)  # Add this field for image upload

    def __str__(self):
        return self.game_name