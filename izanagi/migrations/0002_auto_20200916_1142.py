# Generated by Django 2.1.2 on 2020-09-16 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('izanagi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mgeneral',
            name='valueFloat1',
            field=models.FloatField(max_length=30),
        ),
        migrations.AlterField(
            model_name='mgeneral',
            name='valueFloat2',
            field=models.FloatField(verbose_name='小数２'),
        ),
        migrations.AlterField(
            model_name='mgeneral',
            name='valueFloat3',
            field=models.FloatField(verbose_name='小数３'),
        ),
        migrations.AlterField(
            model_name='mgeneral',
            name='valueFloat4',
            field=models.FloatField(verbose_name='小数４'),
        ),
        migrations.AlterField(
            model_name='mgeneral',
            name='valueFloat5',
            field=models.FloatField(verbose_name='小数５'),
        ),
        migrations.AlterField(
            model_name='mgeneral',
            name='valueNum1',
            field=models.IntegerField(verbose_name='数値１'),
        ),
        migrations.AlterField(
            model_name='mgeneral',
            name='valueNum2',
            field=models.IntegerField(verbose_name='数値２'),
        ),
        migrations.AlterField(
            model_name='mgeneral',
            name='valueNum3',
            field=models.IntegerField(verbose_name='数値３'),
        ),
        migrations.AlterField(
            model_name='mgeneral',
            name='valueNum4',
            field=models.IntegerField(verbose_name='数値４'),
        ),
        migrations.AlterField(
            model_name='mgeneral',
            name='valueNum5',
            field=models.IntegerField(verbose_name='数値５'),
        ),
    ]