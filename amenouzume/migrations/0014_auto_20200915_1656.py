# Generated by Django 2.1.2 on 2020-09-15 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amenouzume', '0013_auto_20200914_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mitem',
            name='safety_amt',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5, verbose_name='安全在庫数'),
        ),
    ]
