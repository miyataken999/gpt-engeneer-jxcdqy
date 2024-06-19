from django import forms
from .models import Jewelry

class JewelryForm(forms.ModelForm):
    class Meta:
        model = Jewelry
        fields = ('name', 'type', 'size', 'shape', 'condition', 'image')