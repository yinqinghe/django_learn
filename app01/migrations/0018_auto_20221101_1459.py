# Generated by Django 3.2.4 on 2022-11-01 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0017_auto_20221101_1455'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='add_time1',
            name='ctime',
        ),
        migrations.AlterField(
            model_name='add_time1',
            name='datetime',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='cctime',
            name='datetime',
            field=models.DateTimeField(blank=True),
        ),
    ]
