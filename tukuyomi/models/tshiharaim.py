from django.db import models
from django.db.models.signals import post_delete
from django.utils.timezone import now
from django.dispatch import receiver
from tukuyomi.models.mbuyer import MBuyer

class TShiharaiM(models.Model):

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

    item_nm = models.CharField(
        verbose_name='品名',
        max_length=30,
        blank=False,
    )

    buyer_cd = models.IntegerField(
        verbose_name='購入者コード',
        blank=False,
    )

    sum_user_amt = models.IntegerField(
        verbose_name='金額',
        blank=False,
    )

    refund_balance = models.IntegerField(
        verbose_name='返金残高',
        blank=False,
        default=0,
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

    # def __str__(self):
    #     """ファイルのURLを返す"""
    #     meta_fields = models._meta.get_fields()
    #     ret = list()
    #     for i, meta_field in enumerate(meta_fields):
    #         if i > 0:
    #             ret.append(meta_field.value)
    #     return ret