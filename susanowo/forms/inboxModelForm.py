from django import forms
from django.db import models
from susanowo.models.ttodo import TTodo

WHERE_DONT_ACTION = (
    ('1','いつかやる'),
    ('2','参考資料'),
    ('3','ごみ箱')
)

# CATEGORY = {
#     '06':'いつかやる',
#     '07':'参考資料',
#     '08':'ゴミ箱',
#     '02':'プロジェクト',
#     '01':'すぐやる',
#     '05':'他人に任せる',
#     '04':'特定の日にやる',
#     '03':'自分でやる',
# }

class InboxModelForm(forms.ModelForm):

    class Meta:
        model = TTodo
        fields = '__all__'
        # widgets = {
        #     'delivery_date': forms.SelectDateWidget
        # }
