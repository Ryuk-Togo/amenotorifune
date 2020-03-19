from django import forms
from django.forms import formsets
from django.forms import models
from tukuyomi.models.tshiharaim import TShiharaiM
from tukuyomi.models.mbuyer import MBuyer
from tukuyomi import tukuyomiConst

class TShiharaiMModelForm(forms.ModelForm):

    id = forms.IntegerField(
        label = 'ID',
        widget = forms.HiddenInput,
        required = False,
    )

    buyer_choice = forms.ChoiceField(
        label = '購入者',
        widget = forms.Select,
        choices = [],
        required = True,
    )

    shiharai_row = forms.IntegerField(
        label = '行',
        widget = forms.HiddenInput,
        required = False,
    )

    delete_flg = forms.BooleanField(
        label = '削除',
        widget = forms.HiddenInput,
        required = False,
        initial = False,
    )

    class Meta:
        model = TShiharaiM
        fields = ('item_nm','sum_user_amt')
        widgets = {
            # 'id': forms.HiddenInput(),
            'item_nm': forms.TextInput(),
        }

    def __init__(self, *args, **kwargs):
        super(TShiharaiMModelForm, self).__init__(*args, **kwargs)
        # self.fields['buyer_choice'].choices = None
        self.fields['buyer_choice'].choices = tukuyomiConst.BUYER_CHOICE

TShiharaiMModelFormSet = formsets.formset_factory(form=TShiharaiMModelForm, extra=0, max_num=1)
