from django.db import models
from django.db.models.signals import post_delete
from django.utils.timezone import now
from django.dispatch import receiver

class TShiharaiM(models.Model):

    userId = models.CharField(
        verbose_name='利用者コード',
        max_length=30,
        blank=False,
    )

    usedDate = models.DateField(
        verbose_name='利用日',
        blank=False,
    )

    shopName = models.CharField(
        verbose_name='店名',
        max_length=30,
        blank=False,
    )

    asseerCd = models.CharField(
        verbose_name='資産名コード',
        max_length=30,
        blank=False,
    )

    itemNm = models.CharField(
        verbose_name='品名',
        max_length=30,
        blank=False,
    )

    buyerCd = models.CharField(
        verbose_name='購入者コード',
        max_length=30,
        blank=False,
    )

    sumUserAmt = models.IntegerField(
        verbose_name='金額',
        blank=False,
    )

    refundBalance = models.IntegerField(
        verbose_name='返金残高',
        blank=False,
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
