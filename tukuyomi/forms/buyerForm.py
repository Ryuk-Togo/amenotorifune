from django import forms
from django.forms import formsets
from django.forms import models
from tukuyomi.models.mbuyer import MBuyer

class BuyerModelForm(forms.ModelForm):

    class Meta:
        model = MBuyer
        fields = ('id','buyerNm')
        widgets = {
            'buyerNm': forms.TextInput(),
        }
