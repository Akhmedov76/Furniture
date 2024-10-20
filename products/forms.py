from django import forms
from .models import ColorModel


class ColorPickerForm(forms.ModelForm):

    class Meta:
        model = ColorModel
        fields = ['name', 'code']
        widgets = {
            'code': forms.TextInput(attrs={'type': 'color'})
        }
