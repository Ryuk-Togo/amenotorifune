from django import forms
from django.db import models
from susanowo.models.tshiryou import TShiryou

class TShiryouModelForm(forms.ModelForm):
    
    class Meta:
        model = TShiryou
        fields = '__all__'
