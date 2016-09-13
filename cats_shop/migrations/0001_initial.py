# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cats_shop.models
import enumfields.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='cats')),
            ],
        ),
        migrations.CreateModel(
            name='Breed',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('desc', models.CharField(max_length=256, blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
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
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
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
