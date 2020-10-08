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
    TKondateRecipe,
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
    
    class Meta:
        model = MRecipe
        fields = ('id','recipe_name','url')
        widgets = {
            'id': forms.HiddenInput(),
            'place_name': forms.TextInput(),
            'url': forms.TextInput(),
        }

# レシピ材料入力画面
class RecipeItemForm(forms.ModelForm):
    
    item_name = forms.CharField(label='材料',required=False,
        widget=forms.TextInput(),
    )

    class Meta:
        model = MRecipeItem
        fields = ('id','recipe_id','item_id','item_amt')
        widgets = {
            'id': forms.HiddenInput(),
            'item_id': forms.HiddenInput(),
            'item_amt': forms.TextInput(),
        }

RecipeItemFormSet = formsets.formset_factory(form=RecipeItemForm, extra=0,)

# 献立
class KondateForm(forms.ModelForm):
    
    class Meta:
        model = TKondate
        fields = ('id','recipe_date','is_noon','is_main')
        widgets = {
            'id': forms.HiddenInput(),
            'recipe_date': forms.TextInput(),
            'is_noon': forms.BooleanField(
                label='午前／午後',
                required=False,
                widget=forms.CheckboxInput(
                    attrs={'class': 'check'}
                ),
            ),
            'is_main': forms.BooleanField(
                label='主菜／副菜',
                required=False,
                widget=forms.CheckboxInput(
                    attrs={'class': 'check'}
                ),
            ),
        }

# 献立のレシピ
class KondateRecipeForm(forms.ModelForm):
    
    recipe_name = forms.CharField(label='レシピ名',required=False,
        widget=forms.TextInput(),
    )

    class Meta:
        model = TKondateRecipe
        fields = ('id','recipe_id')
        widgets = {
            'id': forms.HiddenInput(),
            'recipe_id': forms.HiddenInput(),
        }

KondateItemFormSet = formsets.formset_factory(form=RecipeItemForm, extra=0,)

class ItemModelForm(forms.ModelForm):
    
    class Meta:
        model = MItem
        fields = ('id','item_name')
        widgets = {
            'id': forms.HiddenInput(),
            'item_name': forms.TextInput(),
        }

