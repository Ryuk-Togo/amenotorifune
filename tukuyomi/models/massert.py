from django.db import models
from django.db.models.signals import post_delete
from django.utils.timezone import now
from django.dispatch import receiver

class MAssert(models.Model):

    user_id = models.CharField(
        verbose_name='利用者コード',
        max_length=30,
        blank=False,
    )

    assertNm = models.CharField(
        verbose_name='資産名',
        max_length=60,
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
