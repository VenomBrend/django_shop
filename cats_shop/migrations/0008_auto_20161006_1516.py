# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cats_shop', '0007_auto_20161006_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='photo',
            field=models.ImageField(upload_to=''),
        ),
    ]
