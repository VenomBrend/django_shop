# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cats_shop.models
import enumfields.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('photo', models.ImageField(upload_to=b'cats')),
            ],
        ),
        migrations.CreateModel(
            name='Breed',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, null=True)),
                ('desc', models.CharField(max_length=256, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sex', enumfields.fields.EnumIntegerField(enum=cats_shop.models.GenderEnum)),
                ('date', models.DateField()),
                ('desc', models.CharField(max_length=256, blank=True)),
                ('price', models.DecimalField(max_digits=5, decimal_places=2)),
                ('breed', models.ForeignKey(to='cats_shop.Breed')),
            ],
        ),
        migrations.CreateModel(
            name='CatColor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
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
        migrations.AddField(
            model_name='cat',
            name='cat_color',
            field=models.ForeignKey(to='cats_shop.CatColor'),
        ),
        migrations.AddField(
            model_name='album',
            name='cat',
            field=models.ForeignKey(to='cats_shop.Cat'),
        ),
    ]
