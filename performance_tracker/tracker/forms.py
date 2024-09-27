from django import forms
from .models import PerformanceData

class PerformanceDataForm(forms.ModelForm):
    class Meta:
        model = PerformanceData
        fields = ['date', 'income', 'expenses']