#! /usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask
import httplib2
import json


# Flask app call
app = Flask(__name__)

DB_URL = "http://127.0.0.1:5984/"
RECIPES_VIEW = "recipes/_design/by_url/_view/"
RCPS_URL = DB_URL + RECIPES_VIEW

HEADER = { 'Host': 'www.paodeacucar.com.br',
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:36.0) Gecko/20100101 Firefox/36.0',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' }

#Cookie: __utma=184304057.836521572.1415134357.1421258726.1421260917.4; __utmz=184304057.1415134357.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); OAID=19f76bc89b59552173fa9bcef8998ad9; __utmc=184304057; ep.selected_store=3; ep.store_name_3=S%26%23xe3%3Bo%20Paulo; ep.currency_code_3=BRL; ep.language_code_3=pt-BR; SLIBeacon_1128597223=QNRNNXFTN1421255805432TCPYTDTHQ; SLI2_1128597223=QNRNNXFTN1421255805432TCPYTDTHQ.1421260918324.2.2; SLI4_1128597223=1421260929535; JSESSIONID=FA760EE1B56CDF8E44790B08E48985D2; ep.SYS=0; __utmb=184304057.3.10.1421260917; __utmt=1; SLI1_1128597223=QNRNNXFTN1421255805432TCPYTDTHQ.1421260918324.2.2; ep.ping=0; ep.lastTimeCheckedBasket=1421260918418

 
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
    # Fetch ingredients price from Suppliers
    p_ids = []
    for p in recipe['products']:
        p_ids.append(eval(p['o_id']))
    p_ids = str(p_ids)[1:-1].replace(' ', '')
    found, result = get_prices(p_ids)
    if(not found):
        return result
    prices = json.loads(result[16: -1])['products']
    for p in prices:
        print str(p)
    #sfor product in recipe['products']:
        
    
    
    return 'hold my ass for a sec loading: ' + recipe['name']


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
    app.debug = True
    app.run(host='0.0.0.0')