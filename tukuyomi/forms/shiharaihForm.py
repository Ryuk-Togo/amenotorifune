from django import forms
from django.forms import formsets
from django.forms import models
from tukuyomi.models.tshiharaih import TShiharaiH
from tukuyomi.models.massert import MAssert

class TShiharaiHModelForm(forms.ModelForm):

    class Meta:
        model = TShiharaiH
        fields = ('used_date','shop_name','used_amt','receipt')
        widgets = {
            'shop_name': forms.TextInput(),
        }

class TShiharaiHDeleteModelForm(forms.ModelForm):
    
    class Meta:
        model = TShiharaiH
        fields = ('used_date','shop_name','used_amt','receipt')
        widgets = {
            'used_date': forms.TextInput(attrs={'readonly': 'readonly'}),
            'shop_name': forms.TextInput(attrs={'readonly': 'readonly'}),
            'used_amt': forms.TextInput(attrs={'readonly': 'readonly'}),
            'receipt': forms.TextInput(attrs={'readonly': 'readonly'}),
        }
