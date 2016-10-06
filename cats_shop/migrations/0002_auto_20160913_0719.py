from django.db import models, migrations

import lxml.html as html
import requests
from urllib.parse import urljoin

from django_shop.settings import MEDIA_ROOT

import os


response = requests.get('https://en.wikipedia.org/wiki/List_of_cat_breeds')

# Parse the body into a tree
parsed_body = html.fromstring(response.text)

def breeds_parse(response, parsed_body):
    # Perform xpaths on the tree
    breeds_list = parsed_body.xpath('//table/tr/td/a/text()')
    return breeds_list

breeds_list = breeds_parse(response, parsed_body)

os.makedirs(MEDIA_ROOT + '/cats', exist_ok=True)

def images_parse(response, parsed_body, breeds_list):

    #We are taking onle first 10 images
    images_route_list = parsed_body.xpath("//table/tr/td[7]/a/@href")[0:10]

    # Convert any relative urls to absolute urls
    images_absolute_route_list = [urljoin("https://en.wikipedia.org", image_route) for image_route in images_route_list]

    # For creating images names appropriate for breeds, didn't find best way ._.
    breeds_list = breeds_list[::-1]

    for url in images_absolute_route_list:
        response = requests.get(url)
        parsed_body = html.fromstring(response.text)

        # Pulling alone element from list
        full_image_url = parsed_body.xpath("//div[@class='fullImageLink']/a/@href")[0]

        full_image_absolute_url = urljoin("https:", full_image_url)

        r = requests.get(full_image_absolute_url)

        with open(MEDIA_ROOT + '/cats/%s' % breeds_list.pop(), 'wb') as f:
            f.write(r.content)

images_parse(response, parsed_body, breeds_list)


def breeds_filling(apps, schema_editor):
    Breed = apps.get_model('cats_shop', 'Breed')
    db_alias = schema_editor.connection.alias
    for breed in breeds_list:
        Breed.objects.using(db_alias).create(name=breed, desc='')


def colors_filling(apps, schema_editor):
    CatColor = apps.get_model('cats_shop', 'CatColor')
    db_alias = schema_editor.connection.alias
    colors = ['black', 'gray', 'white']
    for color in colors:
        CatColor.objects.using(db_alias).create(name=color)


class Migration(migrations.Migration):
    dependencies = [
        ('cats_shop', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(breeds_filling),
        migrations.RunPython(colors_filling),
]