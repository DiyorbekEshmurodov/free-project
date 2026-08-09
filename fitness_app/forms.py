from django import forms
from .models import *

class HisobotForm(forms.ModelForm):
    class Meta:
        model = FitnessPlan
        fields = '__all__'
        widgets = {
            'goal': forms.TextInput(attrs={'class': 'form-control'}),
            'kunlik': forms.TextInput(attrs={'class': 'form-control'}),
            'haftalik': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'oylik': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'yillik': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }
