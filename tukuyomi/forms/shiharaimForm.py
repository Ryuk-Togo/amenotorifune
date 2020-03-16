from django import forms
from django.forms import formsets
from django.forms import models
from tukuyomi.models.tshiharaim import TShiharaiM
from tukuyomi.models.mbuyer import MBuyer

class TShiharaiMModelForm(forms.ModelForm):

    buyer_choice = forms.ChoiceField(
        label = '購入者',
        widget = forms.Select,
        choices = [],
        required = False,
    )

    # shiharai_row = forms.IntegerField(
    #     label = '行',
    #     widget = forms.HiddenInput,
    #     required = False,
    # )

    class Meta:
        model = TShiharaiM
        fields = ('id','user_id','item_nm','buyer_cd','sum_user_amt')
        widgets = {
            'id': forms.HiddenInput(),
            'item_nm': forms.TextInput(),
            # 'buyer_cd': forms.Select,
        }

    def __init__(self,user_id, *args, **kwargs):
        super(TShiharaiMModelForm, self).__init__(*args, **kwargs)
        self.fields['buyer_cd'].choices = [(' ','')] + [(buyer.id, buyer.buyerNm) for buyer in MBuyer.objects.filter(user_id=user_id).order_by('buyerNm')]

TShiharaiMModelFormSet = formsets.formset_factory(form=TShiharaiMModelForm, extra=0,)
# TShiharaiMModelFormSet = forms.inlineformset_factory(parent_model=TShiharaiM, form=TShiharaiMModelForm, extra=0,)
