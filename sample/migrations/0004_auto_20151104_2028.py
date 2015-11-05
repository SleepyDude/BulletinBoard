# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0003_user_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile',
            name='user_zip',
            field=models.IntegerField(null=True),
        ),
    ]
