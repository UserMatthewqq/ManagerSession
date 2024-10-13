from django import forms
from .models import SaveFilesModell


class SaveFilesForm(forms.ModelForm):
    class Meta:
        model = SaveFilesModell
        fields = ['room_id', 'filee', 'time']
