from django.db import models
from django.utils.timezone import now

WHERE_DONT_ACTION = (
    ('1','いつかやる'),
    ('2','参考資料'),
    ('3','ごみ箱')
)

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
        max_length=1,
        choices=WHERE_DONT_ACTION,
        blank=True,
    )
    delivery_date = models.DateField(
        verbose_name='期限',
        blank=True,
        default=now,
    )
    single_action = models.BooleanField(
        verbose_name='アクションは１つ？',
        blank=True,
    )
    can_do_tow_minite = models.BooleanField(
        verbose_name='２分以内で終わる？',
        blank=True,
    )
    should_myself = models.BooleanField(
        verbose_name='自分でやるべき',
        blank=True,
    )
    should_do_than_2min = models.BooleanField(
        verbose_name='特定の日にやるべき？',
        blank=True,
    )
    user_id = models.CharField(
        verbose_name='ログインID',
        max_length=6,
        blank=True,
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
