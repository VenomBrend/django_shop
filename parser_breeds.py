import sys

if sys.version.startswith('2'):
    from urllib2 import urlopen
else:
    from urllib.request import urlopen

from lxml.html import fromstring
from pyquery import PyQuery as pq


URL = 'https://en.wikipedia.org/wiki/List_of_cat_breeds'
ITEM_PATH = 'table.wikitable tr '






def parse_breed(url, item_path):

    f = urlopen(url)
    list_html = f.read().decode('utf-8')
    list_doc = fromstring(list_html)
    rows = list_doc.cssselect(item_path)[1:]
    breeds= []
    for row in rows:
        cols = row.cssselect('td')
        a = cols[0].cssselect('a')
        breeds.append(pq(a).attr('title'))
    return breeds


def get_breeds():
  parse_breed(URL,ITEM_PATH)



def main():
    print(parse_breed(URL,ITEM_PATH))


if __name__ == '__main__':
    main()