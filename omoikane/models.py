from django.db import models
from django.utils.timezone import now
from django.shortcuts import render

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
    admin_auth = models.BooleanField(
        verbose_name='管理者権限',
        blank=False,
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

def get_upload_dir(instance, filename):
    return 'omoikane/icon/{0}/{1}'.format(instance.menu_id,instance.icon)

class MMenu(models.Model):
    # id = models.AutoField(
    #     primary_key=True
    # )  # 自動的に追加されるので定義不要
    menu_id = models.IntegerField(
        verbose_name='メニューid',
    )
    menu_name = models.CharField(
        verbose_name='システム名称',
        max_length=50,
        help_text='システム名を入力してください',
        default=''
    )
    url = models.CharField(
        verbose_name='URL',
        max_length=100,
        help_text='システムのURLを入力してください',
        default=''
    )
    icon = models.ImageField(
        verbose_name='アイコン',
        upload_to=get_upload_dir,
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

class MAuth(models.Model):
    user_id = models.CharField(
        verbose_name='ユーザID',
        max_length=30,
        help_text='システムにログインするIDを入力してください',
        blank=False,
    )

    menu_id = models.CharField(
        verbose_name='メニューID',
        max_length=30,
        blank=True,
    )
