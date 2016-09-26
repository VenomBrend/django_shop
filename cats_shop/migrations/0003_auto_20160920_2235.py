# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('cats_shop', '0002_auto_20160913_0719'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='name',
            field=models.CharField(max_length=64, null=True, verbose_name=b'Contact name'),
        ),
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
