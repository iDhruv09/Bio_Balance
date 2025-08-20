def generate_recommendations(health_data):
    recs = []
    if not health_data:
        return ["No data available."]

    latest = health_data[-1]  # last entry

    # Recommendations based on conditions
    if latest.sleep_hours < 6:
        recs.append("😴 Improve your sleep schedule. Try at least 7-8 hrs.")
    if latest.heart_rate > 100:
        recs.append("❤️ High heart rate detected, reduce caffeine/stress.")
    if latest.stress_level > 7:
        recs.append("🧘 Try meditation or breathing exercises.")
    if latest.glucose > 140:
        recs.append("🍚 High glucose spike! Avoid high-GI meals at dinner.")
    if latest.spo2 < 95:
        recs.append("🌬️ Low oxygen saturation detected. Check breathing or consult a doctor if persistent.")

    # Only if no alerts were triggered
    if len(recs) == 0:
        recs.append("✅ Keep it up! Your health metrics look good.")

    return recs
