from django import forms
from .models import SaveImageModel


class SaveImageForm(forms.ModelForm):
    class Meta:
        model = SaveImageModel
        fields = ['room_id', 'coordinates', 'src', 'image']
