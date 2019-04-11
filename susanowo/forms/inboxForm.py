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
        label='詳細',
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
    
class InboxModelForm(forms.ModelForm):

    class Meta:
        model = TTodo
        fields = '__all__'
        widgets = {
            'title' : forms.TextInput(attrs={'size':30}),
            'discription' : forms.Textarea(attrs={'cols':80,'rows':5}),
            'should_action' : forms.BooleanField(attrs={'label':"行動を起こす必要があるか？"}),
            'where_dont_action' : forms.RadioSelect(attrs={''}),
            'single_action' : forms.BooleanField(attrs={'label':"アクションは１つ？",required:False}),
            'single_action' : forms.BooleanField(attrs={'label':"２分以内で終わる？",required:False}),
            'single_action' : forms.BooleanField(attrs={'label':"自分でやるべき",required:False}),
            'single_action' : forms.BooleanField(attrs={'label':"特定の日にやるべき？",required:False}),
            'user_id' : forms.TextInput(attrs={'size':6}),
            'category' : forms.TextInput(attrs={'size':6})
        }

    
# class InboxModelForm(forms.ModelForm):
    
#     class Meta:
#         model = TTodo
#         fields = ('title','discription','should_action','where_dont_action','single_action','can_do_tow_minite','should_myself','should_do_than_2min')
#         widgets = {
#             'title' : forms.TextInput(attrs={'size':30}),
#             'discription' : forms.Textarea(attrs={'cols':80,'rows':5}),
#             'should_action' : forms.BooleanField(attrs={'label':"行動を起こす必要があるか？"}),
#             'where_dont_action' : forms.RadioSelect(attrs={''}),
#             'single_action' : forms.BooleanField(attrs={'label':"アクションは１つ？",required:False}),
#             'single_action' : forms.BooleanField(attrs={'label':"２分以内で終わる？",required:False}),
#             'single_action' : forms.BooleanField(attrs={'label':"自分でやるべき",required:False}),
#             'single_action' : forms.BooleanField(attrs={'label':"特定の日にやるべき？",required:False}),
#             'user_id' : forms.TextInput(attrs={'size':6}),
#             'category' : forms.TextInput(attrs={'size':6})
#         }
