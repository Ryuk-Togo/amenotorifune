from django import forms
from susanowo.models.ttodo import TTodo

WHERE_DONT_ACTION = (
    ('1','いつかやる'),
    ('2','参考資料'),
    ('3','ごみ箱')
)

class InboxForm(forms.Form):
    title = forms.CharField(
        label='タイトル',
        max_length=30,
        required=True,
        widget=forms.TextInput()
    )
    
    discription = forms.CharField(
        label='タスクの詳細',
        required=True,
        widget=forms.Textarea(attrs={'rows':4, 'cols':40})
    )

    should_action = forms.BooleanField(
        label='行動を起こす必要があるか？',
        required=False,
    )
    
    where_dont_action = forms.ChoiceField(
        label='',
        widget=forms.RadioSelect,
        choices=WHERE_DONT_ACTION,
        required=True,
    )
    
    single_action = forms.BooleanField(
        label='アクションは１つ？',
        required=False,
    )
    
    can_do_tow_minite = forms.BooleanField(
        label='２分以内で終わる？',
        required=False,
    )
    
    should_myself = forms.BooleanField(
        label='自分でやるべき',
        required=False,
    )
    
    should_do_than_2min = forms.BooleanField(
        label='特定の日にやるべき？',
        required=False,
    )
