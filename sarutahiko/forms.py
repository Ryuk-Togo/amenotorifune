from django import forms
from django.forms import formsets
from django.forms import models
from omoikane.models import (
    MUser,
)
from amenouzume.models import (
    MItem,
)
# from sarutahiko.models import (
# )

class LoginModelForm(forms.ModelForm):
    
    class Meta:
        model = MUser
        fields = ('user_id','password')
        widgets = {
            'password': forms.PasswordInput(render_value=True),
        }

