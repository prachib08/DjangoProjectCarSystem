from django import forms
from .models import Car

class CarForm(forms.ModelForm):
    class Meta:
        model= Car
        fields = ['Company','model','year','Price']
        labels = {
            'Company': 'company',
            'model':'Model',
            'year':'Year',
            'Price':'price'
        }

        widgets = {
            'Company':forms.TextInput(attrs={'class':'form-control'}),
            'model':forms.TextInput(attrs={'class':'form-control'}),
            'year':forms.NumberInput(attrs={'class':'form-control'}),
            'Price':forms.NumberInput(attrs={'class':'form-control'}),
        }