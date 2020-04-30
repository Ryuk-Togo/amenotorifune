from django import forms
from django.forms import formsets
from django.forms import models
from omoikane.models import (
    MUser,
)
from amenouzume.models import (
    MPlace,
    MItem,
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