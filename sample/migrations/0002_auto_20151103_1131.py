# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bulletin',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=30)),
                ('text', models.TextField()),
                ('date', models.DateField()),
            ],
            options={
                'db_table': 'bulletin',
            },
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
