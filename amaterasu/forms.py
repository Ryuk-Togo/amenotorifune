from django import forms
from django.forms import formsets
from django.forms import models
from omoikane.models import (
    MUser,
)
from amaterasu.models import (
    MSite,
)

class LoginModelForm(forms.ModelForm):
    
    class Meta:
        model = MUser
        fields = ('user_id','password')
        widgets = {
            'password': forms.PasswordInput(render_value=True),
        }

class SiteModelForm(forms.ModelForm):

    re_login_user_pw = forms.CharField(
        label='再パスワード',
        max_length=50,
        required=True,
        widget=forms.PasswordInput(render_value=True),
    )
    
    class Meta:
        model = MSite
        fields = ('site_name','login_user_id','login_user_pw','site_url')
        widgets = {
            'login_user_pw': forms.PasswordInput(render_value=True),
        }

    def clean(self):
        cleaned_data = super().clean()
        v_login_user_pw = cleaned_data.get('login_user_pw') 
        v_re_login_user_pw = cleaned_data.get('re_login_user_pw')

        if v_login_user_pw!=v_re_login_user_pw:
            raise forms.ValidationError("パスワードが一致しません。")

        return cleaned_data

