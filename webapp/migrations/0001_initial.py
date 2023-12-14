# Generated by Django 5.0 on 2023-12-14 10:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70, verbose_name='Наименование')),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70, verbose_name='Наименование')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Полное описание')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('edit_time', models.DateTimeField(auto_now=True, verbose_name='Время обновления')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='webapp.status', verbose_name='Статус')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='webapp.type', verbose_name='Тип')),
            ],
        ),
    ]
