from django import forms
from .models import *

class RegisterForm(forms.ModelForm):
    class Meta:
        model = UserDetail
        fields = '__all__'
        widgets = {
            'username': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Foydalanuvchi nomini kiriting'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Elektron pochtangiz'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Parol'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'buyi': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Bo\'yingiz (sm)'}),
            'vazni': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Vazningiz (kg)'}),
            'jinsi': forms.Select(attrs={'class': 'form-control'}, choices=[('Erkak', 'Erkak'), ('Ayol', 'Ayol')]),
        }