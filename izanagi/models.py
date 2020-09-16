from django.db import models
from django.utils.timezone import now

class MGeneral(models.Model):
    
    key1 = models.CharField(
        verbose_name='キー１',
        max_length=30,
        blank=False,
        default='',
    )

    key2 = models.CharField(
        verbose_name='キー２',
        max_length=30,
        blank=False,
        default='',
    )

    key3 = models.CharField(
        verbose_name='キー３',
        max_length=30,
        blank=False,
        default='',
    )

    # 文字列値
    value1 = models.CharField(
        verbose_name='文字列１',
        max_length=30,
        blank=True,
        default='',
    )

    value2 = models.CharField(
        verbose_name='文字列２',
        max_length=30,
        blank=True,
        default='',
    )

    value3 = models.CharField(
        verbose_name='文字列３',
        max_length=30,
        blank=True,
        default='',
    )

    value4 = models.CharField(
        verbose_name='文字列４',
        max_length=30,
        blank=True,
        default='',
    )

    value5 = models.CharField(
        verbose_name='文字列５',
        max_length=30,
        blank=True,
        default='',
    )

    # 数値
    valueNum1 = models.IntegerField(
        verbose_name='数値１',
        default=0,
    )

    valueNum2 = models.IntegerField(
        verbose_name='数値２',
        default=0,
    )

    valueNum3 = models.IntegerField(
        verbose_name='数値３',
        default=0,
    )

    valueNum4 = models.IntegerField(
        verbose_name='数値４',
        default=0,
    )

    valueNum5 = models.IntegerField(
        verbose_name='数値５',
        default=0,
    )

    # 小数値
    valueFloat1 = models.FloatField(
        verbose_name='小数１',
        default=0.000,
    )

    valueFloat2 = models.FloatField(
        verbose_name='小数２',
        default=0.000,
    )

    valueFloat3 = models.FloatField(
        verbose_name='小数３',
        default=0.000,
    )

    valueFloat4 = models.FloatField(
        verbose_name='小数４',
        default=0.000,
    )

    valueFloat5 = models.FloatField(
        verbose_name='小数５',
        default=0.000,
    )
