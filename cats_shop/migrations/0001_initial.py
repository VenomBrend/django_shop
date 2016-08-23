# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import enumfields.fields
import cats_shop.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Breed',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('sex', enumfields.fields.EnumIntegerField(enum=cats_shop.models.GenderEnum)),
                ('date', models.DateField()),
                ('desc', models.CharField(max_length=256)),
                ('photo', models.ImageField(upload_to='cats')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
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
    ]
