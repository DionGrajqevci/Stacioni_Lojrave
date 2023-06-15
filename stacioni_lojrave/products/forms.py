from django import forms
from .models import Futbollisti,Review

class FutbollistiForm(forms.ModelForm):
    class Meta:
        model = Futbollisti
        fields = ('name', 'position', 'team')

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']