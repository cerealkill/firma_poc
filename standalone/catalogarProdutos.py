#! /usr/bin/python
# -*- coding: utf-8 -*-
import urllib
import re

from catalogoProdutos import Produto
from BeautifulSoup import BeautifulSoup
from anonBrowser import anonBrowser
from couchdbHandler import Couch


DATABASEURL = 'http://127.0.0.1:5984'
INGREDIENTES_DATABASE = 'dicionario_ingredientes'
PRODUTOS_DATABASE = 'catalogo_produtos'
QUANTIDADE_RESULTADOS = '20'


def get_serch_url(term, category):
    return 'http://busca.paodeacucar.com.br/search?' + \
        'p=Q&lbc=paodeacucar' + \
        '&ts=custom&w=' + term + \
        '&isort=price&method=and&view=list&cnt=' + \
        QUANTIDADE_RESULTADOS + \
        '&af=categoria:' + category


def save(data):
    'Saves page to disk cache'
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


def fetch_produtos(url, categoria, ingrediente):
    wholehtml = open_URL(url)
    print '\n[+] Returned Products'
    soup = BeautifulSoup(wholehtml)
    prodhtml = soup.findAll("div", "boxProduct")
    lista_produto = []
    for html in prodhtml:
        desc = html.findChild("h3").text
        img = get_URL(html.findChild("img").get('src'))
        id_ = get_id(html.findChild("footer").get('id'))
        produto = Produto('pda', id_, desc, categoria, None, img, ingrediente)
        lista_produto.append(produto)
        print '[.]\t\t Produto: ' + desc

    return lista_produto


def main():

    couch = Couch(url_=DATABASEURL, session_=None)
    couch.del_db(PRODUTOS_DATABASE)
    idb = couch.fetch_db(INGREDIENTES_DATABASE)
    pdb = couch.fetch_db(PRODUTOS_DATABASE)

    for id in idb:
        i = idb[id]
        ingrediente = i['desc']
        ingrediente_busca = urllib.quote(ingrediente)
        print '---------------------------------------------------------' + \
            '---------------------------------------------------------\n' + \
            '[+] Begin quering ''Fornecedor'' for: ' + i['desc']

        categorias = i['categoria']
        for c in categorias:
            categoria_busca = urllib.quote(c['nome'])
            url = get_serch_url(ingrediente_busca, categoria_busca)
            produtos = fetch_produtos(url, c, i['desc'])
            for p in produtos:
                couch.add_doc(pdb, dict(p))

        map_function = 'function(doc) {if (doc.ingrediente == "' + \
            ingrediente + '") {emit(null, {"id": doc.o_id, "desc":' + \
            ' doc.desc, "img": doc.img, "preco": doc.preco}); } }'
        view_doc = couch.create_view_doc(i['desc'], map_function)
        couch.add_view_doc(pdb, view_doc)

    print '[+] Done.'

if __name__ == '__main__':
        main()
