# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cats_shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('photo', models.ImageField(upload_to=b'cats')),
            ],
        ),
        migrations.RemoveField(
            model_name='cat',
            name='photo',
        ),
        migrations.AlterField(
            model_name='breed',
            name='desc',
            field=models.CharField(max_length=256, blank=True),
        ),
        migrations.AlterField(
            model_name='cat',
            name='desc',
            field=models.CharField(max_length=256, blank=True),
        ),
        migrations.AddField(
            model_name='album',
            name='cat',
            field=models.ForeignKey(to='cats_shop.Cat'),
        ),
    ]
