from django import forms
from django.forms import formsets
from django.forms import models
from omoikane.models import (
    MUser,
)
from amenouzume.models import (
    MPlace,
)

class LoginModelForm(forms.ModelForm):
    
    class Meta:
        model = MUser
        fields = ('user_id','password')
        widgets = {
            'password': forms.PasswordInput(render_value=True),
        }

class PlaceModelForm(forms.ModelForm):
    
    class Meta:
        model = MPlace
        fields = ('place_name',)
        widgets = {
            'place_name': forms.TextInput(),
        }

class PlaceDeleteModelForm(forms.ModelForm):
    
    class Meta:
        model = MPlace
        fields = ('place_name',)
        widgets = {
            'place_name': forms.TextInput(attrs={'readonly': 'readonly'}),
        }

