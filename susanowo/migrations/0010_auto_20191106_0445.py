# Generated by Django 2.1.2 on 2019-11-06 04:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('susanowo', '0009_ttodo_deleted'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ttodo',
            old_name='should_do_than_2min',
            new_name='should_do_oneday',
        ),
    ]
