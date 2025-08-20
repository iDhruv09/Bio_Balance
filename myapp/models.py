from django.db import models

class HealthData(models.Model):
    user = models.CharField(max_length=100)
    date = models.DateField()
    sleep_hours = models.FloatField()
    heart_rate = models.IntegerField()
    stress_level = models.IntegerField()
    glucose = models.FloatField()

    def __str__(self):
        return f"{self.user} - {self.date}"
