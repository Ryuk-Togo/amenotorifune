# Generated by Django 2.1.2 on 2019-12-17 15:10

from django.db import migrations, models
import susanowo.models.tshiryou


class Migration(migrations.Migration):

    dependencies = [
        ('susanowo', '0015_auto_20191212_0432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tshiryou',
            name='attach',
            field=models.FileField(upload_to=susanowo.models.tshiryou.get_upload_dir, verbose_name='添付ファイル'),
        ),
    ]
