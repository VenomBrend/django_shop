# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models, migrations
from urllib.request import urlopen
#from urllib2 import urlopen
from lxml.html import fromstring
from pyquery import PyQuery as pq

URL = 'https://en.wikipedia.org/wiki/List_of_cat_breeds'  # site's url for parser
ITEM_PATH = 'table.wikitable tr '  # tags to start


def parse_breed(url, item_path):
    f = urlopen(url)
    list_html = f.read().decode('utf-8')
    list_doc = fromstring(list_html)
    rows = list_doc.cssselect(item_path)[1:]  # 1 bf first tr miss
    breeds = []
    for row in rows:
        cols = row.cssselect('td')  # select td
        a = cols[0].cssselect('a')  # select a in td
        breeds.append(pq(a).attr('title'))
    return breeds


def filling_breeds(apps, schema_editor):
    breeds_list = parse_breed(URL, ITEM_PATH)
    Breed = apps.get_model('cats_shop', 'Breed')
    db_alias = schema_editor.connection.alias    
    for breed in breeds_list:
        if breed != None:
            Breed.objects.using(db_alias).create(name=breed, desc='')
            


class Migration(migrations.Migration):
    dependencies = [
        ('cats_shop', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(filling_breeds),
    ]
