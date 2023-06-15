from django import forms
from .models import Futbollisti

class FutbollistiForm(forms.ModelForm):
    class Meta:
        model = Futbollisti
        fields = ['name', 'position', 'team']