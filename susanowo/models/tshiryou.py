from django.db import models
from django.utils.timezone import now

class TShiryou(models.Model):
    # id = models.AutoField(
    #     primary_key=True
    # )  # 自動的に追加されるので定義不要
    todo_id = models.IntegerField(
        verbose_name='タスクのid',
    )
    attach = models.FileField(
        # upload_to='susanowo/shiryou/',
        verbose_name='添付ファイル',
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

    def __str__(self):
        """ファイルのURLを返す"""
        return self.file.url