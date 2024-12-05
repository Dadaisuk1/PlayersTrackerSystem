from django import forms
from .models import Analytics

class AnalyticsForm(forms.ModelForm):
    class Meta:
        model = Analytics
        fields = ['kills', 'death', 'assist', 'win_loss']
