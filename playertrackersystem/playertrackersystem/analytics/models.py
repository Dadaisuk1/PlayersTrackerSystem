from django.db import models

class Analytics(models.Model):
    analytics_id = models.AutoField(primary_key=True)
    kills = models.IntegerField()
    death = models.IntegerField()
    assist = models.IntegerField()
    win_loss = models.CharField(max_length=10)

    def __str__(self):
        return f"Analytics {self.analytics_id}"
