# Generated by Django 2.1.2 on 2020-04-28 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amenouzume', '0004_auto_20200428_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mplace',
            name='place_name',
            field=models.CharField(max_length=100, verbose_name='場所名'),
        ),
    ]