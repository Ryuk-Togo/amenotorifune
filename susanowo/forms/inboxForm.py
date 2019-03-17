from django import forms

WHERE_DONT_ACTION = (
    ('1','いつかやる'),
    ('2','参考資料'),
    ('3','ごみ箱')
)

class InboxForm(forms.Form):
    title = forms.CharField(
        label="タイトル",
        max_length=30,
        required=True,
        widget=forms.TextInput()
    )
    discription = forms.CharField(
        label="内容",
        max_length=200,
        required=False
    )
    should_action = forms.BooleanField(
        label="行動を起こす必要があるか？",
        required=False
    )
    where_dont_action = forms.ChoiceField(
        label='今やらない',
        widget=forms.RadioSelect,
        choices=WHERE_DONT_ACTION,
        required=True
    )
    single_action = forms.BooleanField(
        label="行動を起こす必要があるか？",
        required=False
    )
    can_do_tow_minite = forms.BooleanField(
        label="２分以内で終わる？",
        required=False
    )
    should_myself = forms.BooleanField(
        label="自分でやるべき",
        required=False
    )
    should_do_than_2min = forms.BooleanField(
        label="特定の日にやるべき？",
        required=False
    )
    user_id = forms.CharField(max_length=6)
    category = forms.CharField(max_length=6)
