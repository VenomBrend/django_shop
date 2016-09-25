# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('cats_shop', '0003_auto_20160920_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='photo',
            field=models.ImageField(upload_to='cats'),
        ),
        migrations.AlterField(
            model_name='order',
            name='closed',
            field=models.DateTimeField(verbose_name='Closed at', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Opened at'),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='order',
            name='is_closed',
            field=models.BooleanField(verbose_name='Is closed', default=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='is_shipped',
            field=models.BooleanField(verbose_name='Is shipped', default=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='name',
            field=models.CharField(verbose_name='Contact name', null=True, max_length=64),
        ),
    ]
