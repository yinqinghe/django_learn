# Generated by Django 3.2.4 on 2022-11-01 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0013_auto_20221101_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_time',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='add_time',
            name='dates',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
