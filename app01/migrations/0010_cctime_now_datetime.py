# Generated by Django 3.2.4 on 2022-11-01 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0009_remove_cctime_now_datetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='cctime',
            name='now_datetime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
