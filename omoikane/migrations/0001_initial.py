# Generated by Django 2.1.2 on 2019-12-20 00:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(default='', help_text='システムにログインするIDを入力してください', max_length=30, verbose_name='ユーザID')),
                ('user_name', models.CharField(default='', help_text='お名前を入力してください', max_length=30, verbose_name='ユーザ名')),
                ('password', models.CharField(default='', help_text='システムにログインするパスワードを入力してください', max_length=30, verbose_name='パスワード')),
                ('create_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='登録日時')),
                ('create_pg_id', models.CharField(blank=True, max_length=30)),
                ('create_user_id', models.CharField(blank=True, max_length=6)),
                ('update_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='更新日時')),
                ('update_pg_id', models.CharField(blank=True, max_length=30)),
                ('update_user_id', models.CharField(blank=True, max_length=6)),
            ],
        ),
    ]
