from django import forms
from django.forms import formsets
from django.forms import models
from tukuyomi.models.massert import MAssert

class AssertModelForm(forms.ModelForm):

    class Meta:
        model = MAssert
        fields = ('id','assertNm')
        widgets = {
            'assertNm': forms.TextInput(),
        }

# AssertListModelFormSet = formsets.formset_factory(form=AssertModelForm, extra=0,)
