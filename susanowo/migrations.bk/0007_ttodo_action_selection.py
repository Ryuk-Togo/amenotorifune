# Generated by Django 2.1.2 on 2019-05-14 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('susanowo', '0006_auto_20190512_1439'),
    ]

    operations = [
        migrations.AddField(
            model_name='ttodo',
            name='action_selection',
            field=models.CharField(choices=[('1', 'いつかやる'), ('2', '参考資料'), ('3', 'ごみ箱')], max_length=1, null=True),
        ),
    ]
