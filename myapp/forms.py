from django import forms
from .models import HealthData

class HealthDataForm(forms.ModelForm):
    class Meta:
        model = HealthData
        fields = ['user', 'date', 'sleep_hours', 'heart_rate', 'stress_level', 'glucose']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'sleep_hours': forms.NumberInput(attrs={'step': '0.1', 'class': 'form-control'}),
            'heart_rate': forms.NumberInput(attrs={'class': 'form-control'}),
            'stress_level': forms.NumberInput(attrs={'min': 1, 'max': 10, 'class': 'form-control'}),
            'glucose': forms.NumberInput(attrs={'step': '0.1', 'class': 'form-control'}),
        }
