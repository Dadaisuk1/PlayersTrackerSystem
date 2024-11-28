# models.py
from django.db import models

class Item(models.Model):
    item_id = models.AutoField(primary_key=True)  # Auto-incremented primary key
    item_name = models.CharField(max_length=69)
    item_type = models.CharField(max_length=69)
    cost = models.FloatField()

    def __str__(self):
        return self.item_name
