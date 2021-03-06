# Generated by Django 2.1.2 on 2019-05-17 05:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('susanowo', '0017_ttodo_create_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='ttodo',
            name='update_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='更新日時'),
        ),
        migrations.AlterField(
            model_name='muser',
            name='create_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='登録日時'),
        ),
        migrations.AlterField(
            model_name='muser',
            name='create_pg_id',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='muser',
            name='create_user_id',
            field=models.CharField(blank=True, max_length=6),
        ),
        migrations.AlterField(
            model_name='muser',
            name='update_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='更新日時'),
        ),
        migrations.AlterField(
            model_name='muser',
            name='update_pg_id',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='muser',
            name='update_user_id',
            field=models.CharField(blank=True, max_length=6),
        ),
    ]
