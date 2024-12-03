from django.db import models

class Match(models.Model):
    match_id = models.AutoField(primary_key=True)
    match_date = models.DateField()
    inventory = models.CharField(max_length=69)

    def __str__(self):
        return f"Match {self.match_id} - {self.inventory}"
