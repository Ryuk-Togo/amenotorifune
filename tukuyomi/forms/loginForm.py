from django import forms
from django.forms import formsets
from django.forms import models
from omoikane.models import MUser

class LoginModelForm(forms.ModelForm):

    class Meta:
        model = MUser
        fields = ('user_id','password')
        widgets = {
            'password': forms.PasswordInput(render_value=True),
        }

    def clean(self):
        cleaned_data = super().clean()
        v_user_id = cleaned_data.get('user_id') 
        v_password = cleaned_data.get('password')
        user = None
        try:
            user = MUser.objects.get(user_id=v_user_id)
        except:
            raise forms.ValidationError("ユーザIDが存在しません。")

        if not user.password==v_password:
            raise forms.ValidationError("パスワードが違います。")

        return cleaned_data
