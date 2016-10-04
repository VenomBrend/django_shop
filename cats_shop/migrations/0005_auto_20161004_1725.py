# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cats_shop.models
import enumfields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cats_shop', '0004_auto_20160925_2032'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='is_closed',
        ),
        migrations.RemoveField(
            model_name='order',
            name='is_shipped',
        ),
        migrations.AddField(
            model_name='cat',
            name='in_stock',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=enumfields.fields.EnumIntegerField(enum=cats_shop.models.OrderStatusEnum, default=1),
        ),
    ]
