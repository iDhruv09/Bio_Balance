from django.db import models

class HealthData(models.Model):
    user = models.CharField(max_length=100)
    date = models.DateField()
    sleep_hours = models.FloatField()
    heart_rate = models.IntegerField()
    stress_level = models.IntegerField()
    glucose = models.FloatField()
    spo2 = models.IntegerField(default=98)  # New field, default healthy range
    def __str__(self):
        return f"{self.user} - {self.date}"
