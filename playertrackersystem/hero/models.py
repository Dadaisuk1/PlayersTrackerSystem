from django.db import models

# Create your models here.
class Hero(models.Model):
    hero_id = models.AutoField(primary_key = True)
    hero_name = models.CharField(max_length = 69)
    role = models.CharField(max_length = 69)
    match = models.CharField(max_length = 69)
    image = models.ImageField(upload_to = 'images/', blank = True, null = True)

    def __str__(self):
        return self.hero_name