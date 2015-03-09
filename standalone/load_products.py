#! /usr/bin/python
# -*- coding: utf-8 -*-
import urllib
import re

from products import Product, ProductId
from BeautifulSoup import BeautifulSoup
from browser import anonBrowser
from cozy_couch import Couch


DATABASEURL = 'https://firma.iriscouch.com'
INGREDIENTS_DATABASE = 'ingredients'
PRODUCTS_DATABASE = 'products'
MAX_RESULTS = '20'


def get_serch_url(term, category):
    return 'http://busca.paodeacucar.com.br/search?' + \
        'p=Q&lbc=paodeacucar' + \
        '&ts=custom&w=' + term + \
        '&isort=price&method=and&view=list&cnt=' + \
        MAX_RESULTS + \
        '&af=categoria:' + category


def save(data):
    'Saves page to disk cached page'
    file_ = open('./search_results.html', 'w+')
    file_.truncate()
    print >>file_, data


def open_URL(url):
    'Anonymize url request and fetch page'
    ab = anonBrowser()
    ab.anonymize()
    print '[*] Fetching page \n[+] URL: ' + url
    response = ab.open(url)
    html = response.read()
#   save(html)
    for cookie in ab.cookie_jar:
        print '[+] Added cookie: ' + str(cookie)
    return html


def get_id(text):
    finder = re.compile('^\d+')
    return int(finder.findall(text)[0])


def get_URL(text):
    return 'http://www.paodeacucar.com.br' + text


def fetch_produtos(url, category, ingredient):
    wholehtml = open_URL(url)
    print '\n[+] Returned Products'
    soup = BeautifulSoup(wholehtml)
    prodhtml = soup.findAll("div", "boxProduct")
    products = []
    for html in prodhtml:
        desc = html.findChild("h3").text
        img = get_URL(html.findChild("img").get('src'))
        id_ = get_id(html.findChild("footer").get('id'))
        produto = Product(ProductId('pda', id_), desc, category, None, img, ingredient)
        products.append(produto)
        print '[.]\t\t Product: ' + desc

    return products


def main():

    couch = Couch(url_=DATABASEURL, session_=None)
    couch.del_db(PRODUCTS_DATABASE)
    idb = couch.fetch_db(INGREDIENTS_DATABASE)
    pdb = couch.fetch_db(PRODUCTS_DATABASE)

    views = {}

    for id in idb:
        i = idb[id]
        ingredient = i['desc']
        search_term = urllib.quote(ingredient)
        print '---------------------------------------------------------' + \
            '---------------------------------------------------------\n' + \
            '[+] Begin quering ''Fornecedor'' for: ' + i['desc']

        categorias = i['category']
        for c in categorias:
            categoria_busca = urllib.quote(c['name'])
            url = get_serch_url(search_term, categoria_busca)
            produtos = fetch_produtos(url, c, i['desc'])
            for p in produtos:
                couch.add_doc(pdb, dict(p))

        map_function = 'function(doc) {if (doc.ingredient == "' + \
            ingredient + '") {emit(null, {"id": doc.p_id.o_id, "desc":' + \
            ' doc.desc, "img": doc.img, "price": doc.price}); } }'
        
        views[i['desc']] = {'map': map_function} 
         
    view_doc = couch.create_view_doc('by_ingredient', views)
    couch.add_view_doc(pdb, view_doc)

    print '[+] Done.'

if __name__ == '__main__':
        main()
