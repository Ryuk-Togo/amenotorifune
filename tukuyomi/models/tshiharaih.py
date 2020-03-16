from django.db import models
from django.db.models.signals import post_delete
from django.utils.timezone import now
from django.dispatch import receiver

class TShiharaiH(models.Model):

    user_id = models.CharField(
        verbose_name='利用者コード',
        max_length=30,
        blank=False,
    )

    used_date = models.DateField(
        verbose_name='利用日',
        blank=False,
    )

    shop_name = models.CharField(
        verbose_name='店名',
        max_length=30,
        blank=False,
    )

    assert_cd = models.IntegerField(
        verbose_name='資産名コード',
        blank=False,
    )

    used_amt = models.IntegerField(
        verbose_name='利用金額',
        blank=False,
    )

    receipt = models.ImageField(
        verbose_name='レシート',
        max_length=30,
        blank=True,
    )

    create_date = models.DateTimeField(
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
        return self.receipt.url

# モデル削除後に`file_field`を削除する。
@receiver(post_delete, sender=TShiharaiH)
def delete_file(sender, instance, **kwargs):
    instance.receipt.delete(False)