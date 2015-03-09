#! /usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask
from flask.templating import render_template
from decimal import Decimal

import httplib2
import json
import urllib
import locale
import re


# Flask app call
app = Flask(__name__)

DB_URL = "https://firma.iriscouch.com/"
RECIPES_VIEW = "recipes/_design/by_url/_view/"
RCPS_URL = DB_URL + RECIPES_VIEW
PRODUCTS_VIEW = "products/_design/by_ingredient/_view/"
PRDS_URL = DB_URL + PRODUCTS_VIEW

HEADER = { 'Host': 'www.paodeacucar.com.br',
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:36.0) Gecko/20100101 Firefox/36.0',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' }


 
@app.route('/')
def index():
    return '<!DOCTYPE html><html lang="pt-BR"><head>\
            <title>Cardápio Maroto</title>\
            <meta charset="utf-8"></head>\
            <body><h1>Receitas Marotas do Rafinha ;)</h1>\
            Não perdemos por esperar!</body></html>'


@app.route('/recipes/<recipe_url>')
def show_recipe(recipe_url):
    # Fetch recipe document from database
    found, result = get_db_data(RCPS_URL + recipe_url)
    if(not found):
        return result
    recipe = json.loads(result)['rows'][0]['value']
    # Get total cook time sum
    ttime = 0
    for s in recipe['steps']:
        if(s['time']):
            time = re.search('([\d]+)', s['time']).group()
            ttime += int(time)
        
    return render_template('recipe.html', recipe=recipe, tprice='25,15', ttime=ttime)


@app.route('/recipes/<recipe_url>/checkout')
def show_recipe_checkout(recipe_url):
    # Fetch recipe document from database
    found, result = get_db_data(RCPS_URL + recipe_url)
    if(not found):
        return result
    recipe = json.loads(result)['rows'][0]['value']
    # Reach for product list by ingredient
    p_ids = []
    products = {}
    for i in recipe['ingredients']:
        ingredient = urllib.quote(i['name'])
        found, result = get_db_data(PRDS_URL + ingredient)
        if(found):
            result = json.loads(result)['rows']
            priced = []
            for p in result:
                priced.append(p['value'])
                p_ids.append(p['value']['id'])
            products[i['name']] = priced
    # Fetch ingredients price from Suppliers
    p_ids = str(p_ids)[1:-1].replace(' ', '')
    found, result = get_prices(p_ids)
    if(not found):
        return result
    prices = json.loads(result[16: -1])['products']
    # Fill prices on products and order list by price
    for ik in products.iterkeys():
        ps = []
        for p in products[ik]:
            for pr in prices:
                if(p['id']==pr['id'] and pr['stock']):
                    p['price'] = pr['price']
                    ps.append(p)
                    break
        products[ik] = ps
        products[ik].sort(key=lambda k: k['price'])
    # Get featured products sum
    tprice = Decimal()
    featured = []
    for f in recipe['products']:
        for l in products.itervalues():
            found = False
            for p in l:
                if(eval(f['o_id'])==p['id']):
                    tprice += Decimal(p['price'].replace(',','.'))
                    featured.append(p)
                    found = True
                    break
            if(found): break
    recipe['products'] = featured
        
    return render_template('checkout.html', recipe=recipe, products=products)


def get_prices(product_ids):
    response, content = httplib2.Http().request('http://www.paodeacucar.com.br', 'GET', None, HEADER)  # @UnusedVariable
    cookie = response['set-cookie']
    headers = HEADER.copy()
    headers['Cookie'] = cookie
    liveprice = "http://www.paodeacucar.com.br/livePrice?jsonp=true&productIds="
    response, content = httplib2.Http().request(liveprice + product_ids, 'GET', None, headers)  # @UnusedVariable
    if(response['status']=='200'):
        return (True, content)
    else:
        print '[!] Failed to get data from PDA.'
        return (False, 'Dados nao encontrados')


def get_db_data(url):
    headers = {}
    headers['Accept'] = 'application/json, text/javascript'    
    response, content = httplib2.Http().request(url, 'GET', None, headers)  # @UnusedVariable

    if(response['status']=='200'):
        return (True, content)
    else:
        print '[!] Failed to get data from db.'
        return (False, 'Página não encontrada'.decode('utf-8'))


if __name__ == '__main__':
    locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')
    app.debug = True
    app.run(host='0.0.0.0')