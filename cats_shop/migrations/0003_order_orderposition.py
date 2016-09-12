# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cats_shop', '0002_auto_20160901_1706'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'Opened at')),
                ('closed', models.DateTimeField(null=True, verbose_name=b'Closed at', blank=True)),
                ('is_closed', models.BooleanField(default=False, verbose_name=b'Is closed')),
                ('is_shipped', models.BooleanField(default=False, verbose_name=b'Is shipped')),
                ('customer', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
            },
        ),
        migrations.CreateModel(
            name='OrderPosition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.ForeignKey(related_name='positions', to='cats_shop.Order')),
                ('product', models.ForeignKey(to='cats_shop.Cat')),
            ],
            options={
                'verbose_name': 'Order position',
                'verbose_name_plural': 'Order positions',
            },
        ),
    ]
