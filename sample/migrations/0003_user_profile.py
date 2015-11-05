# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sample', '0002_auto_20151103_1131'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_profile',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('full_name', models.CharField(max_length=30)),
                ('birthday', models.DateField()),
                ('user_adress', models.CharField(max_length=35)),
                ('user_city', models.CharField(max_length=20)),
                ('user_state', models.CharField(max_length=20)),
                ('user_country', models.CharField(max_length=20)),
                ('user_zip', models.IntegerField()),
                ('user', models.ForeignKey(unique=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'profile',
            },
        ),
    ]
