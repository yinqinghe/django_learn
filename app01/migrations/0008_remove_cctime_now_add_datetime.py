# Generated by Django 3.2.4 on 2022-11-01 05:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0007_alter_cctime_datetime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cctime',
            name='now_add_datetime',
        ),
    ]
