# Generated by Django 3.2.4 on 2022-11-01 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0018_auto_20221101_1459'),
    ]

    operations = [
        migrations.AddField(
            model_name='add_time1',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
