# Generated by Django 2.1.2 on 2020-10-14 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sarutahiko', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mrecipeitem',
            name='row',
            field=models.IntegerField(default=0, verbose_name='行'),
        ),
    ]
