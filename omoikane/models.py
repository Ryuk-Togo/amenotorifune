from django.db import models
from django.utils.timezone import now

# Create your models here.
class MUser(models.Model):
    user_id = models.CharField(
        verbose_name='ユーザID',
        max_length=30,
        help_text='システムにログインするIDを入力してください',
        blank=False,
    )
    user_name = models.CharField(
        verbose_name='ユーザ名',
        max_length=30,
        help_text='お名前を入力してください',
        default=''
    )
    password = models.CharField(
        verbose_name='パスワード',
        max_length=30,
        help_text='システムにログインするパスワードを入力してください',
        blank=False,
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