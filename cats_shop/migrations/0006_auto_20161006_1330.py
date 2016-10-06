# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cats_shop', '0005_auto_20161004_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='cat',
            field=models.ForeignKey(to='cats_shop.Cat', related_name='album'),
        ),
        migrations.AlterField(
            model_name='cat',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
