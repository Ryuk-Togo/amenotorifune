from django.db import models
from django.utils.timezone import now

WHERE_DONT_ACTION = (
    ('1','いつかやる'),
    ('2','参考資料'),
    ('3','ごみ箱')
)

CATEGORY = {
    '06':'いつかやる',
    '07':'参考資料',
    '08':'ゴミ箱',
    '02':'プロジェクト',
    '01':'すぐやる',
    '05':'他人に任せる',
    '04':'特定の日にやる',
    '03':'自分でやる',
}

class TTodo(models.Model):
    # todo_id = models.AutoField(
    #     primary_key=True
    # )  # 自動的に追加されるので定義不要
    title = models.CharField(
        verbose_name='タイトル',
        max_length=30,
        help_text='タスクのタイトルを入力してください',
    )
    discription = models.CharField(
        verbose_name='タスクの詳細',
        max_length=200,
        help_text='タスクの詳細な内容を入力して下さい',
    )
    should_action = models.BooleanField(
        verbose_name='行動を起こす必要があるか？',
        blank=True,
    )
    action_selection = models.CharField(
        verbose_name='行動',
        max_length=1,
        choices=WHERE_DONT_ACTION,
        blank=True,
    )
    delivery_date = models.DateField(
        verbose_name='期限',
        blank=True,
        null=True,
    )
    single_action = models.BooleanField(
        verbose_name='アクションは１つ？',
        blank=True,
    )
    can_do_tow_minite = models.BooleanField(
        verbose_name='２分以上かかりそう？',
        blank=True,
    )
    should_myself = models.BooleanField(
        verbose_name='自分でやるべき',
        blank=True,
    )
    should_do_oneday = models.BooleanField(
        verbose_name='特定の日にやるべき？',
        blank=True,
    )
    user_id = models.CharField(
        verbose_name='ログインID',
        max_length=6,
        blank=True,
    )
    category = models.CharField(
        verbose_name='カテゴリー',
        max_length=2,
        blank=True,
    )
    completed = models.BooleanField(
        verbose_name='完了',
        blank=True,
        default=False,
    )
    deleted = models.BooleanField(
        verbose_name='削除',
        blank=True,
        default=False,
    )
    create_date = models.DateTimeField(
        verbose_name='登録日時',
        blank=True,
        default=now,
    )
    create_pg_id = models.CharField(
        max_length=30,
        blank=True,
    )
    create_user_id = models.CharField(
        max_length=6,
        blank=True,
    )
    update_date = models.DateTimeField(
        verbose_name='更新日時',
        blank=True,
        default=now,
    )
    update_pg_id = models.CharField(
        max_length=30,
        blank=True,
    )
    update_user_id = models.CharField(
        max_length=6,
        blank=True,
    )

    def category_name(self):
        if self.category in CATEGORY:
            return CATEGORY.get(self.category)
        else:
            return ''
        # return self.category

def computeCategory(todo):
    category = '99'
    if todo.should_action:
        if todo.single_action:
            category = '02'

        if not todo.can_do_tow_minite:
            category = '01'

        if todo.should_myself:
            category = '03'
        else:
            category = '05'

        if todo.should_do_oneday:
            category = '04'

    else:
        if todo.action_selection == '1':
            category = '06'
        elif todo.action_selection == '2':
            category = '07'
        elif todo.action_selection == '3':
            category = '08'

    return category