# Generated by Django 3.2.4 on 2022-11-05 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app02', '0002_book_atime'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='ctime',
            field=models.DateTimeField(auto_created=True, null=True),
        ),
    ]
