# Generated by Django 3.2.4 on 2022-11-01 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0011_cctime_now_add_datetime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cctime',
            name='now_add_datetime',
        ),
        migrations.AddField(
            model_name='cctime',
            name='booleans',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='cctime',
            name='ctime',
            field=models.TimeField(default=0),
        ),
        migrations.AlterField(
            model_name='cctime',
            name='ipadd',
            field=models.GenericIPAddressField(default=0),
        ),
        migrations.AlterField(
            model_name='lmsuser',
            name='mobile',
            field=models.CharField(max_length=11, verbose_name='手机'),
        ),
    ]
