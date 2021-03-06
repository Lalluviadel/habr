# Generated by Django 3.2.14 on 2022-07-14 19:52

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=128)),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('is_active', models.BooleanField(db_index=True, default=True, verbose_name='раздел активен')),
            ],
            options={
                'verbose_name': 'Раздел сайта',
                'verbose_name_plural': 'Разделы сайта',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=128, verbose_name='наименование')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Теги',
                'verbose_name_plural': 'Тег',
                'ordering': ('tag_name',),
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='время создания')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('is_active', models.BooleanField(db_index=True, default=False, verbose_name='статья активна')),
                ('title', models.CharField(max_length=128, verbose_name='заголовок')),
                ('body', models.CharField(max_length=100000, verbose_name='тело')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='articles.category')),
                ('tag', models.ManyToManyField(to='articles.Tag')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
                'ordering': ['-registration_time'],
            },
        ),
    ]
