from django.db import models
from django.contrib.auth.hashers import make_password

class Player(models.Model):
    playerID = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)  # Ensure unique usernames
    password = models.CharField(max_length=128)  # Use enough space for hashed passwords

    def save(self, *args, **kwargs):
        # Hash the password if it's not already hashed
        if not self.password.startswith('pbkdf2_sha256$'):  # Avoid re-hashing an already hashed password
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username
