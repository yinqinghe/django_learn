# Generated by Django 3.2.4 on 2022-11-01 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0006_auto_20221101_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cctime',
            name='datetime',
            field=models.DateTimeField(verbose_name=''),
        ),
    ]
