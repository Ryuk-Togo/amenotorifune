# Generated by Django 2.1.2 on 2019-05-17 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('susanowo', '0014_auto_20190517_0455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ttodo',
            name='user_id',
            field=models.CharField(blank=True, max_length=6, verbose_name='ログインID'),
        ),
    ]
