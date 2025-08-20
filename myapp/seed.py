from .models import HealthData
from datetime import date, timedelta
import random

def run():
    users = ["Dhruv", "Amit", "Sneha"]
    today = date.today()

    for user in users:
        for i in range(7):  # last 7 days
            HealthData.objects.create(
                user=user,
                date=today - timedelta(days=i),
                sleep_hours=random.uniform(5, 9),
                heart_rate=random.randint(60, 110),
                stress_level=random.randint(1, 10),
                glucose=random.uniform(90, 160),
            )
    print("✅ Dummy data added!")



