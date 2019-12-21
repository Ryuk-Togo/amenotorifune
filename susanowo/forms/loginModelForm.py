from django import forms
from omoikane.models import MUser

class MUserModelForm(forms.ModelForm):
    class Meta:
        model = MUser
        fields = ('user_id','password')
        # fields = '__all__'
        widgets = {
            'password': forms.PasswordInput(render_value=True),
        }
    
    # def clean_user_id(self):
    #     v_user_id = self.cleaned_data['user_id'] 
    #     user = None
    #     try:
    #         user = MUser.objects.get(user_id=v_user_id)
    #     except:
    #         raise forms.ValidationError("ユーザIDが存在しません。")
    #     return user

    # def clean_password(self):
    #     v_user_id = self.cleaned_data['user_id'] 
    #     v_password = self.cleaned_data['password'] 
    #     user = MUser.objects.get(user_id=v_user_id)

    #     if not user.password == v_password:
    #         raise forms.ValidationError("パスワードが違います。")
    #     return v_password
    
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
