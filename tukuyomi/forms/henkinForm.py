from django import forms
from django.forms import formsets
from django.forms import models
from tukuyomi.models.tshiharaim import TShiharaiM
from tukuyomi.models.mbuyer import MBuyer
from tukuyomi import tukuyomiConst

class HenkinHeaderForm(forms.Form):
    
    buyer_name = forms.ChoiceField(
        required=True,
        label='購入者',
        widget=forms.Select(attrs={'buyer_id': 'buyer_name',})
    )

    row_count = forms.IntegerField(
        required=False,
        label='件数',
        widget=forms.HiddenInput()
    )

    sum_refund_balance = forms.IntegerField(
        required=True,
        label='返金額',
    )

class HenkinListForm(forms.ModelForm):

    id = forms.IntegerField(
        label = 'ID',
        widget = forms.HiddenInput,
        required = False,
    )

    is_selected = forms.BooleanField(
        required=False,
        label='選択',
        widget=forms.CheckboxInput(attrs={'class':'is_selected'})
    )

    assert_nm = forms.CharField(
        required=False,
        label='資産名',
        widget=forms.TextInput(attrs={'readonly':'readonly'}),
    )

    moto_refund_balance = forms.IntegerField(
        label = '入力前返金額',
        widget = forms.HiddenInput,
        required = False,
    )

    class Meta:
        model = TShiharaiM
        # fields = ('id','user_id','used_date','shop_name','assert_cd','item_nm','buyer_cd','sum_user_amt','refund_balance')
        fields = ('user_id','used_date','shop_name','assert_cd','item_nm','buyer_cd','sum_user_amt','refund_balance')
        widgets = {
            # 'id': forms.HiddenInput(),
            'user_id': forms.HiddenInput(),
            'used_date': forms.TextInput(attrs={'readonly': 'readonly'}),
            'shop_name': forms.TextInput(attrs={'readonly': 'readonly'}),
            'assert_cd': forms.HiddenInput(),
            'item_nm': forms.TextInput(attrs={'readonly': 'readonly'}),
            'buyer_cd': forms.HiddenInput(),
            'sum_user_amt': forms.TextInput(attrs={'readonly': 'readonly'}),
            'refund_balance': forms.TextInput(attrs={'class': 'refund_balance'}),
        }
