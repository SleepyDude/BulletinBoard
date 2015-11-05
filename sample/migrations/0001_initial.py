# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('login', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('time', models.DateTimeField()),
            ],
            options={
                'db_table': 'profile',
            },
        ),
    ]
