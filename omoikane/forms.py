from django import forms
from django.db import models
from omoikane.models import (
    MUser,
    MMenu,
    MAuth,
)

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

# class UserInputModelForm(forms.ModelForm):

#     password1 = forms.CharField(label='パスワード(確認)',
#         widget=forms.PasswordInput(render_value=True),
#     )

#     class Meta:
#         model = MUser
#         fields = ('user_id','user_name','password')
#         widgets = {
#             'password': forms.PasswordInput(render_value=True),
#         }

#     def clean(self):
#         cleaned_data = super().clean()
#         v_user_id = cleaned_data.get('user_id') 
#         v_user_name = cleaned_data.get('user_name') 
#         v_password = cleaned_data.get('password')
#         v_password1 = cleaned_data.get('password1')
#         user = None
#         try:
#             user = MUser.objects.get(user_id=v_user_id)
#         except:
#             pass

#         if not user is None:
#             raise forms.ValidationError("ユーザIDが存在します。")

#         # if not user.user_id is None:
#         #     raise forms.ValidationError("ユーザIDが存在します。")

#         if not v_password==v_password1:
#             raise forms.ValidationError("パスワード(確認)とパスワードが違います。")

#         return cleaned_data

class UserInputModelForm(forms.ModelForm):

    password1 = forms.CharField(label='パスワード(確認)',
        widget=forms.PasswordInput(render_value=True),
    )

    class Meta:
        model = MUser
        fields = ('user_id','user_name','password')
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput(render_value=True),
        }

    def clean(self):
        cleaned_data = super().clean()
        v_user_id = cleaned_data.get('user_id') 
        v_user_name = cleaned_data.get('user_name') 
        v_password = cleaned_data.get('password')
        v_password1 = cleaned_data.get('password1')
        user = None
        try:
            user = MUser.objects.get(user_id=v_user_id)
        except:
            pass

        if not user is None:
            raise forms.ValidationError("ユーザIDが存在します。")

        if not v_password==v_password1:
            raise forms.ValidationError("パスワード(確認)とパスワードが違います。")

        return cleaned_data

class UserModifyModelForm(forms.ModelForm):
    
    password_now = forms.CharField(label='現在のパスワード',required=False,
        widget=forms.PasswordInput(render_value=True),
    )
    password1 = forms.CharField(label='新しいパスワード',required=False,
        widget=forms.PasswordInput(render_value=True),
    )
    re_password1 = forms.CharField(label='新しいパスワード(確認)',required=False,
        widget=forms.PasswordInput(render_value=True),
    )

    class Meta:
        model = MUser
        fields = ('user_id','user_name')
        widgets = {
            'user_id': forms.TextInput(attrs={'readonly': 'readonly'}),
            # 'user_name': forms.TextInput(attrs={'require': False}),
            # 'password': forms.PasswordInput(render_value=True),
        }

    def clean(self):
        cleaned_data = super().clean()
        v_user_id = cleaned_data.get('user_id') 
        v_user_name = cleaned_data.get('user_name') 
        # v_password = cleaned_data.get('password')
        v_password＿now = cleaned_data.get('password_now')
        v_password1 = cleaned_data.get('password1')
        v_re_password1 = cleaned_data.get('re_password1')
        user = None
        try:
            user = MUser.objects.get(user_id=v_user_id)
        except:
            raise forms.ValidationError("ユーザIDが存在しません。")

        if v_password＿now=='':
            if not v_password1=='':
                raise forms.ValidationError("現在のパスワードを入力していないため、パスワードは変更できません。")

            if not v_re_password1=='':
                raise forms.ValidationError("現在のパスワードを入力していないため、パスワードは変更できません。")

        else:
            if not v_password＿now==user.password:
                raise forms.ValidationError("入力したパスワードが違います。")

            if v_password＿now==user.password:
                if not v_password1==v_re_password1:
                    raise forms.ValidationError("新しいパスワードが違います。")

        return cleaned_data

class UserDeleteModelForm(forms.ModelForm):
    
    class Meta:
        model = MUser
        # fields = ('user_id','user_name','password')
        fields = ('user_id','user_name')
        widgets = {
            'user_id': forms.TextInput(attrs={'readonly': 'readonly'}),
            'user_name': forms.TextInput(attrs={'readonly': 'readonly'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        v_user_id = cleaned_data.get('user_id') 
        user = None
        try:
            user = MUser.objects.get(user_id=v_user_id)
        except:
            raise forms.ValidationError("ユーザIDが存在しません。")

        return cleaned_data

class MenuInputModelForm(forms.ModelForm):
    
    class Meta:
        model = MMenu
        fields = ('menu_name','url','icon')

class MenuModifyModelForm(forms.ModelForm):
    
    menu_id = forms.CharField(label='ID',
        widget=forms.HiddenInput(),
    )

    class Meta:
        model = MMenu
        fields = ('menu_name','url','icon')

    def clean(self):
        cleaned_data = super().clean()
        v_menu_id = cleaned_data.get('menu_id')
        # v_menu_id = self.cleaned_data['id']
        # v_menu_id = self.instance.id
        menu = None
        try:
            menu = MMenu.objects.get(id=v_menu_id)
        except:
            raise forms.ValidationError("メニューが存在しません。")

        return cleaned_data

class MenuDeleteModelForm(forms.ModelForm):
    
    menu_id = forms.CharField(label='ID',
        widget=forms.HiddenInput(),
    )

    class Meta:
        model = MMenu
        fields = ('menu_name','url','icon')
        widgets = {
            'menu_name': forms.TextInput(attrs={'readonly': 'readonly'}),
            'url': forms.TextInput(attrs={'readonly': 'readonly'}),
            'icon': forms.TextInput(attrs={'readonly': 'readonly'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        v_menu_id = cleaned_data.get('menu_id') 
        menu = None
        try:
            menu = MMenu.objects.get(pk=v_menu_id)
        except:
            raise forms.ValidationError("メニューが存在しません。")

        return cleaned_data
