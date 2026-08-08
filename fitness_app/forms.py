from django import forms
from .models import *

class HisobotForm(forms.ModelForm):
    class Meta:
        model = Hisobot
        fields = '__all__'

    widgets = {
        'title': forms.TextInput(attrs={'class': 'form-control'}),
        'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
    }
