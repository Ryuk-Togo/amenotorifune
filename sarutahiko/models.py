from django.db import models
from django.utils.timezone import now

# Create your models here.
# レシピマスタ
class MRecipe(models.Model):
    
    user_id = models.CharField(
        verbose_name='利用者コード',
        max_length=30,
        blank=False,
    )

    recipe_name = models.CharField(
        verbose_name='レシピ名',
        max_length=100,
        blank=False,
    )

    url = models.CharField(
        verbose_name='ＵＲＬ',
        max_length=256,
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

# レシピ材料
class MRecipeItem(models.Model):
    
    user_id = models.CharField(
        verbose_name='利用者コード',
        max_length=30,
        blank=False,
    )

    recipe_id = models.CharField(
        verbose_name='レシピコード',
        max_length=30,
        blank=False,
    )

    item_id = models.CharField(
        verbose_name='材料名',
        max_length=100,
        blank=False,
    )

    item_amt = models.IntegerField(
        verbose_name='数量',
        blank=False,
        default=0,
    )

    row = models.IntegerField(
        verbose_name='行',
        blank=False,
        default=0,
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

# 献立
class TKondate(models.Model):
    
    user_id = models.CharField(
        verbose_name='利用者コード',
        max_length=30,
        blank=False,
    )

    recipe_date = models.DateField(
        verbose_name='日付',
        max_length=100,
        blank=False,
    )

    time = models.CharField(
        verbose_name='時間帯',
        max_length=1,
        blank=False,
    )

    is_sub = models.CharField(
        verbose_name='主菜／副菜',
        max_length=100,
        blank=False,
    )

    number_of_people = models.IntegerField(
        verbose_name='人数',
        blank=False,
    )

    recipe_id = models.CharField(
        verbose_name='レシピID',
        max_length=30,
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
