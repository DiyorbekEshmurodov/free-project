from django import forms
from .models import FitnessPlan

class FitnessPlanForm(forms.ModelForm):
    class Meta:
        model = FitnessPlan
        fields = ['title', 'description', 'period_type', 'target_date', 'is_completed']
        widgets = {
            'target_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'period_type': forms.Select(attrs={'class': 'form-control'}),
        }



# from django import forms
# from .models import *
#
# class HisobotForm(forms.ModelForm):
#     class Meta:
#         model = FitnessPlan
#         fields = '__all__'
#         widgets = {
#             'goal': forms.TextInput(attrs={'class': 'form-control'}),
#             'kunlik': forms.TextInput(attrs={'class': 'form-control'}),
#             'haftalik': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
#             'oylik': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
#             'yillik': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
#         }
#
# class GetKunlikForm(forms.ModelForm):
#     model = GetKunlik
#     fields = '__all__'
#     widgets = {
#         'kunlik': forms.TextInput(attrs={'class': 'form-control'}),
#     }
#
# class GetHaftalikForm(forms.ModelForm):
#     model = GetHaftalik
#     fields = '__all__'
#     widgets = {
#         'Dushanba':forms.TextInput(attrs={'class': 'form-control'}),
#         'Seshanba':forms.TextInput(attrs={'class': 'form-control'}),
#         'Chorshanba':forms.TextInput(attrs={'class': 'form-control'}),
#         'Payshanba':forms.TextInput(attrs={'class': 'form-control'}),
#         'Juma':forms.TextInput(attrs={'class': 'form-control'}),
#         'Shanba':forms.TextInput(attrs={'class': 'form-control'}),
#         'Yakshanba':forms.TextInput(attrs={'class': 'form-control'}),
#     }
#
# class GetOylikForm(forms.ModelForm):
#     model = GetOylik
#     fields = '__all__'
#     widgets = {
#         'Yanvar':forms.TextInput(attrs={'class': 'form-control'}),
#         'Fevral':forms.TextInput(attrs={'class': 'form-control'}),
#         'Mart':forms.TextInput(attrs={'class': 'form-control'}),
#         'April':forms.TextInput(attrs={'class': 'form-control'}),
#         'May':forms.TextInput(attrs={'class': 'form-control'}),
#         'Iyun':forms.TextInput(attrs={'class': 'form-control'}),
#         'Iyul':forms.TextInput(attrs={'class': 'form-control'}),
#         'Avgust':forms.TextInput(attrs={'class': 'form-control'}),
#         'Sentabr':forms.TextInput(attrs={'class': 'form-control'}),
#         'Oktaybr':forms.TextInput(attrs={'class': 'form-control'}),
#         'Noyabr':forms.TextInput(attrs={'class': 'form-control'}),
#         'Dekabr':forms.TextInput(attrs={'class': 'form-control'}),
#     }
#
# class GetYillikForm(forms.ModelForm):
#     model = GetYillik
#     fields = '__all__'
#     widgets = {
#         'year_2026': forms.TextInput(attrs={'class': 'form-control'}),
#         'year_2027': forms.TextInput(attrs={'class': 'form-control'}),
#     }