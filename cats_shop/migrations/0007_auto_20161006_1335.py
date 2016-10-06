# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
from random import choice

from django.db import models, migrations

from django_shop.settings import MEDIA_ROOT


def cats_filling(apps, schema_editor):
    Breed = apps.get_model('cats_shop', 'Breed')
    CatColor = apps.get_model('cats_shop', 'CatColor')
    Cat = apps.get_model('cats_shop', 'Cat')
    Album = apps.get_model('cats_shop', 'Album')
    breeds = Breed.objects.all()
    colors = CatColor.objects.all()
    sex = [1, 2]
    price = [25, 20, 15, 55, 33, 11, 22]
    desc = ['Very funny cat', 'Nice, but lazy', 'Very playfull']
    images = os.listdir(MEDIA_ROOT)
    
    for i in range(len(images)):
        cat = Cat(breed=breeds[i], sex=choice(sex), cat_color=choice(colors),
                  desc=choice(desc), price=choice(price))
        cat.save()
        album = Album(cat=cat, photo=images[images.index(breeds[i].name)])
        cat.save()
        album.save()



class Migration(migrations.Migration):

    dependencies = [
        ('cats_shop', '0006_auto_20161006_1330'),
    ]

    operations = [
        migrations.RunPython(cats_filling),
    ]
