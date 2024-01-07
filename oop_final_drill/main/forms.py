from django import forms
from .models import Character, Village, Jutsu

class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = '__all__'

class VillageForm(forms.ModelForm):
    class Meta:
        model = Village
        fields = '__all__'

class JutsuForm(forms.ModelForm):
    class Meta:
        model = Jutsu
        fields = '__all__'
