from django import forms
from django.db import models
from susanowo.models.ttodo import TTodo

WHERE_DONT_ACTION = (
    ('1','いつかやる'),
    ('2','参考資料'),
    ('3','ごみ箱')
)

class InboxModelForm(forms.ModelForm):

    class Meta:
        model = TTodo
        fields = '__all__'
        # widgets = {
        #     'delivery_date': forms.SelectDateWidget
        # }
