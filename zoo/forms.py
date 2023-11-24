from django import forms
from .models import *
from django.contrib.auth.models import User

class BuildingForm(forms.ModelForm):
    class Meta:
        model = Building
        fields = ['name', 'location', 'purpose', 'area', 'floors']
        
        
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']
        
class EnclosureForm(forms.ModelForm):
    class Meta:
        model = Enclosure
        fields = ['enclosure_id', 'square_foot', 'building_id']