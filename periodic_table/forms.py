from django import forms
from .models import Discovery

class DiscoveryForm(forms.ModelForm):
    class Meta:
        model = Discovery
        fields = ['date', 'type', 'discoverer']
        widgets = {
            'date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={'type': 'date'}
            ),
        }
