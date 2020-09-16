from django.db import models
from django.utils.timezone import now

# Create your models here.
class MPlace(models.Model):
    
    user_id = models.CharField(
        verbose_name='利用者コード',
        max_length=30,
        blank=False,
    )

    place_name = models.CharField(
        verbose_name='場所名',
        max_length=100,
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

class MItem(models.Model):
    
    user_id = models.CharField(
        verbose_name='利用者コード',
        max_length=30,
        blank=False,
    )

    item_name = models.CharField(
        verbose_name='品目名',
        max_length=100,
        blank=False,
    )

    safety_amt = models.DecimalField(
        verbose_name='安全在庫数',
        max_digits=5,
        decimal_places=2,
        blank=False,
        default=0.00,
    )

    item_term = models.IntegerField(
        verbose_name='在庫期間',
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

class MItemPlace(models.Model):
    
    user_id = models.CharField(
        verbose_name='利用者コード',
        max_length=30,
        blank=False,
    )

    item_id = models.CharField(
        verbose_name='品目名',
        max_length=100,
        blank=False,
    )

    place_id = models.CharField(
        verbose_name='場所',
        max_length=100,
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

class TStock(models.Model):
    
    user_id = models.CharField(
        verbose_name='利用者コード',
        max_length=30,
        blank=False,
    )

    item_id = models.IntegerField(
        verbose_name='品目ID',
        blank=False,
    )

    place_id = models.IntegerField(
        verbose_name='場所',
        blank=False,
    )

    item_name = models.CharField(
        verbose_name='品目名',
        max_length=100,
        blank=True,
    )

    safety_amt = models.IntegerField(
        verbose_name='安全在庫数',
        blank=False,
        default=0,
    )

    item_amt = models.IntegerField(
        verbose_name='在庫数',
        blank=True,
    )

    download_date = models.DateTimeField(
        verbose_name='ダウンロード日時',
        blank=True,
        default=now,
    )

    upload_date = models.DateTimeField(
        verbose_name='アップロード日時',
        blank=True,
        default=now,
    )

    buy_amt = models.IntegerField(
        verbose_name='購入数',
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

class TStockHistory(models.Model):
    
    user_id = models.CharField(
        verbose_name='利用者コード',
        max_length=30,
        blank=False,
    )

    item_id = models.CharField(
        verbose_name='品目名',
        max_length=100,
        blank=False,
    )

    place_id = models.CharField(
        verbose_name='場所',
        max_length=100,
        blank=False,
    )

    item_name = models.CharField(
        verbose_name='品目名',
        max_length=100,
        blank=True,
    )

    safety_amt = models.IntegerField(
        verbose_name='安全在庫数',
        blank=False,
        default=0,
    )

    item_amt = models.IntegerField(
        verbose_name='在庫数',
        blank=True,
    )

    download_date = models.DateTimeField(
        verbose_name='ダウンロード日時',
        blank=True,
    )

    upload_date = models.DateTimeField(
        verbose_name='アップロード日時',
        max_length=100,
        blank=True,
    )

    buy_amt = models.IntegerField(
        verbose_name='購入数',
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

