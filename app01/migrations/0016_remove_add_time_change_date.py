# Generated by Django 3.2.4 on 2022-11-01 06:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0015_auto_20221101_1448'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='add_time',
            name='change_date',
        ),
    ]
