from django.db import models
from django.utils.timezone import now

# Create your models here.
class MSite(models.Model):
    
    user_id = models.CharField(
        verbose_name='利用者コード',
        max_length=30,
        blank=False,
    )

    site_name = models.CharField(
        verbose_name='サイト名',
        max_length=100,
        blank=False,
    )

    login_user_id = models.CharField(
        verbose_name='ログインID',
        max_length=50,
        blank=False,
    )

    login_user_pw = models.CharField(
        verbose_name='パスワード',
        max_length=50,
        blank=False,
    )

    site_url = models.CharField(
        verbose_name='サイトURL',
        max_length=100,
        blank=True,
    )

    # discription = models.TextField(
    #     verbose_name='サイトの詳細',
    #     help_text='タスクの詳細な内容を入力して下さい',
    #     blank=True,
    # )

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
        max_length=30,
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
        max_length=30,
        blank=True,
    )
