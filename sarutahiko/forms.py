from django import forms
from django.forms import formsets
from django.forms import models
from omoikane.models import (
    MUser,
)
from amenouzume.models import (
    MItem,
)
from sarutahiko.models import (
    MRecipe,
    MRecipeItem,
    TKondate,
    # TKondateRecipe,
)

# ログイン画面
class LoginModelForm(forms.ModelForm):
    
    class Meta:
        model = MUser
        fields = ('user_id','password')
        widgets = {
            'password': forms.PasswordInput(render_value=True),
        }

# レシピ入力画面
class RecipeForm(forms.ModelForm):
    
    id = forms.IntegerField(label='主キー',
        required=False,
        widget=forms.HiddenInput(),
    )
    
    class Meta:
        model = MRecipe
        # fields = ('id','recipe_name','url')
        fields = ('recipe_name','url')
        # fields = '__all__'
        widgets = {
            # 'id': forms.HiddenInput(),
            'recipe_name': forms.TextInput(attrs={'class' : 'recipe_name_class'}),
            'url': forms.TextInput(),
        }

# レシピ材料入力画面
class RecipeItemForm(forms.Form):

    id = forms.IntegerField(label='主キー',
        required=False,
        widget=forms.HiddenInput(),
    )
    
    recipe_id = forms.IntegerField(label='レシピID',
        required=False,
        widget=forms.HiddenInput(attrs={'class' : 'recipe_id_class'}),
    )
    
    item_id = forms.IntegerField(label='材料コード',
        required=False,
        widget=forms.HiddenInput(),
    )

    item_name = forms.CharField(label='材料',
        required=False,
        widget=forms.TextInput(attrs={'class' : 'item_name_class'}),
    )

    item_amt = forms.IntegerField(label='数量',
        required=False,
        widget=forms.TextInput(attrs={'class' : 'item_amt_class'}),
    )

    row = forms.CharField(label='行',
        required=False,
        widget=forms.HiddenInput(),
    )

# 献立
class KondateForm(forms.Form):

    year = forms.IntegerField(label='年',
        required=False,
        widget=forms.HiddenInput(),
    )

    month = forms.IntegerField(label='月',
        required=False,
        widget=forms.HiddenInput(),
    )

    day = forms.IntegerField(label='日',
        required=False,
        widget=forms.HiddenInput(),
    )

# 献立のレシピ
class KondateRecipeForm(forms.Form):

    recipe_name = forms.CharField(
        label='レシピ',
        required=False,
        widget=forms.TextInput(attrs={'class' : 'recipe_name_class'}),
    )

    number_of_people = forms.IntegerField(
        label='人数',
        required=False,
        widget=forms.TextInput(attrs={'class' : 'number_of_people_class'}),
    )

    time = forms.CharField(
        label='時間帯',
        required=False,
        widget=forms.HiddenInput(),
    )

    is_sub = forms.CharField(
        label='主菜／副菜',
        required=False,
        widget=forms.HiddenInput(),
    )

    id = forms.IntegerField(
        label='主キー',
        required=False,
        widget=forms.HiddenInput(),
    )

    recipe_id = forms.CharField(
        label='レシピID',
        required=False,
        widget=forms.HiddenInput(),
    )

class ItemModelForm(forms.ModelForm):
    
    id = forms.IntegerField(label='主キー',
        required=False,
        widget=forms.HiddenInput(),
    )

    item_name_upd = forms.CharField(
        label='変更後',
        required=True,
        widget=forms.TextInput(),
    )
    
    class Meta:
        model = MItem
        fields = ('id','item_name')
        widgets = {
            'id': forms.HiddenInput(),
            'item_name': forms.TextInput(),
        }

class SendRangeForm(forms.Form):

    start_date = forms.DateField(
        label='開始日',
        required=True,
        widget=forms.TextInput(),
    )

    end_date = forms.DateField(
        label='終了日',
        required=True,
        widget=forms.TextInput(),
    )

