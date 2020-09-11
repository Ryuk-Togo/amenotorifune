from django import forms
from django.forms import formsets
from django.forms import models
from omoikane.models import (
    MUser,
)
from amenouzume.models import (
    MPlace,
    MItem,
    MItemPlace,
    TStock,
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

class ItemModelForm(forms.ModelForm):
    
    class Meta:
        model = MItem
        fields = ('item_name','safety_amt','item_term')

class ItemDeleteModelForm(forms.ModelForm):
    
    class Meta:
        model = MItem
        fields = ('item_name','safety_amt','item_term')
        widgets = {
            'item_name': forms.TextInput(attrs={'readonly': 'readonly'}),
            'safety_amt': forms.TextInput(attrs={'readonly': 'readonly'}),
            'item_term': forms.TextInput(attrs={'readonly': 'readonly'}),
        }

class PlaceHeaderForm(forms.Form):
    
    place_name = forms.ChoiceField(
        required=False,
        label='場所名',
        widget=forms.Select(attrs={'place_id': 'place_name',})
    )

class ItemListForm(forms.ModelForm):
    
    is_select = forms.BooleanField(
        label='選択',
        required=False,
        widget=forms.CheckboxInput(
            attrs={'class': 'check'}
        ),
    )

    item_id = forms.CharField(label='品目ID',
        widget=forms.HiddenInput(),
    )

    class Meta:
        model = MItem
        fields = ('id','item_name')
        widgets = {
            'id': forms.HiddenInput(),
            'item_name': forms.TextInput(attrs={'readonly': 'readonly'}),
        }

ItemListFormSet = formsets.formset_factory(form=ItemListForm, extra=0,)

class StockItemForm(forms.ModelForm):

    item_name = forms.CharField(
        label='品目名',
        widget=forms.TextInput(attrs={'readonly': 'readonly'})
    )

    safety_amt = forms.IntegerField(
        label='安全在庫数',
        widget=forms.TextInput(attrs={'readonly': 'readonly'})
    )

    class Meta:
        model = MItemPlace
        fields = ('id','item_id','item_name','safety_amt')
        widgets = {
            'id': forms.HiddenInput(),
            'item_id': forms.HiddenInput(),
            # 'item_name': forms.TextInput(attrs={'readonly': 'readonly'}),
            # 'safety_amt': forms.TextInput(attrs={'readonly': 'readonly'}),
        }

StockItemFormSet = formsets.formset_factory(form=StockItemForm, extra=0,)

class StockDataForm(forms.Form):
    
    is_select = forms.BooleanField(
        label='選択',
        required=False,
        widget=forms.CheckboxInput(
            attrs={'class': 'check'}
        ),
    )

    place_id = forms.CharField(label='在庫場所ID',
        widget=forms.HiddenInput(),
    )

    place_name = forms.CharField(label='在庫場所名',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}),
    )

    item_data = StockItemFormSet()

StockDataFormSet = formsets.formset_factory(form=StockDataForm, extra=0,)

class StockDataFormTest(forms.ModelForm):
    
    class Meta:
        model = TStock
        fields = ('id','user_id','item_id','item_name','place_id','item_amt','safety_amt','buy_amt')
        widgets = {
            'id': forms.TextInput(),
            'user_id': forms.TextInput(),
            'item_id': forms.TextInput(),
            'item_name': forms.TextInput(),
            'place_id': forms.TextInput(),
            'item_amt': forms.TextInput(),
            'safety_amt': forms.TextInput(),
            'buy_amt': forms.TextInput(),
        }
