# Generated by Django 2.1.2 on 2020-10-13 07:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MRecipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=30, verbose_name='利用者コード')),
                ('recipe_name', models.CharField(max_length=100, verbose_name='レシピ名')),
                ('url', models.CharField(blank=True, max_length=256, verbose_name='ＵＲＬ')),
                ('create_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='登録日時')),
                ('create_pg_id', models.CharField(blank=True, max_length=30)),
                ('create_user_id', models.CharField(blank=True, max_length=30)),
                ('update_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='更新日時')),
                ('update_pg_id', models.CharField(blank=True, max_length=30)),
                ('update_user_id', models.CharField(blank=True, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='MRecipeItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=30, verbose_name='利用者コード')),
                ('recipe_id', models.CharField(max_length=30, verbose_name='レシピコード')),
                ('item_id', models.CharField(max_length=100, verbose_name='材料名')),
                ('item_amt', models.IntegerField(default=0, verbose_name='数量')),
                ('create_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='登録日時')),
                ('create_pg_id', models.CharField(blank=True, max_length=30)),
                ('create_user_id', models.CharField(blank=True, max_length=30)),
                ('update_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='更新日時')),
                ('update_pg_id', models.CharField(blank=True, max_length=30)),
                ('update_user_id', models.CharField(blank=True, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='TKondate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=30, verbose_name='利用者コード')),
                ('recipe_date', models.DateField(max_length=100, verbose_name='日付')),
                ('is_noon', models.BooleanField(max_length=100, verbose_name='午前／午後')),
                ('is_main', models.BooleanField(max_length=100, verbose_name='主菜')),
                ('number_of_people', models.IntegerField(verbose_name='人数')),
                ('create_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='登録日時')),
                ('create_pg_id', models.CharField(blank=True, max_length=30)),
                ('create_user_id', models.CharField(blank=True, max_length=30)),
                ('update_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='更新日時')),
                ('update_pg_id', models.CharField(blank=True, max_length=30)),
                ('update_user_id', models.CharField(blank=True, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='TKondateRecipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=30, verbose_name='利用者コード')),
                ('recipe_id', models.CharField(max_length=30, verbose_name='レシピID')),
                ('create_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='登録日時')),
                ('create_pg_id', models.CharField(blank=True, max_length=30)),
                ('create_user_id', models.CharField(blank=True, max_length=30)),
                ('update_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='更新日時')),
                ('update_pg_id', models.CharField(blank=True, max_length=30)),
                ('update_user_id', models.CharField(blank=True, max_length=30)),
            ],
        ),
    ]
