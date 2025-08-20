from django.shortcuts import render, redirect
from .models import HealthData
from .forms import HealthDataForm
from .utils import generate_recommendations

def dashboard_view(request):
    users = HealthData.objects.values_list("user", flat=True).distinct()
    selected_user = request.GET.get("user")

    health_data = []
    recs = []
    latest_data = None

    if selected_user:
        health_data = HealthData.objects.filter(user=selected_user).order_by("date")

        if health_data.exists():
            latest_data = health_data.last()
            recs = generate_recommendations(list(health_data))

    # Ideal ranges (for gauge snapshot)
    ideal_ranges = {
        "sleep_hours": (7, 9),
        "heart_rate": (60, 100),
        "stress_level": (1, 5),
        "glucose": (70, 140),
    }

    return render(request, "dashboard.html", {
        "users": users,
        "selected_user": selected_user,
        "health_data": health_data,
        "latest_data": latest_data,
        "recs": recs,
        "ideal_ranges": ideal_ranges,
    })


def add_data_view(request):
    if request.method == "POST":
        form = HealthDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")  # redirect to dashboard
    else:
        form = HealthDataForm()

    return render(request, "add_data.html", {"form": form})
