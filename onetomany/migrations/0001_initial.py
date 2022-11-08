# Generated by Django 3.2.4 on 2022-10-28 06:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('describe', models.CharField(max_length=100)),
                ('datatime', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': '项目表',
                'db_table': 'project',
            },
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=30)),
                ('ip', models.GenericIPAddressField()),
                ('describe', models.CharField(max_length=100)),
                ('datatime', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': '服务器',
                'db_table': 'server',
            },
        ),
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('describe', models.CharField(max_length=100)),
                ('datatime', models.DateTimeField(auto_now_add=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onetomany.project')),
            ],
            options={
                'verbose_name': '应用表',
                'db_table': 'app',
            },
        ),
    ]
