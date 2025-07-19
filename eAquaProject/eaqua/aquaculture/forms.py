from django import forms
from .models import FishDisease


class FishDiseaseForm(forms.ModelForm):
    class Meta:
        model = FishDisease
        fields = ['name', 'symptoms', 'causes',
                  'prevention', 'treatment', 'severity']
        widgets = {
            'symptoms': forms.Textarea(attrs={'rows': 4}),
            'causes': forms.Textarea(attrs={'rows': 4}),
            'prevention': forms.Textarea(attrs={'rows': 4}),
            'treatment': forms.Textarea(attrs={'rows': 4}),
        }
