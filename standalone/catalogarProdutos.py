#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib
import sys
import json
import re
import couchdb

from catalogoProdutos import Produto
from BeautifulSoup import BeautifulSoup
from anonBrowser import anonBrowser


search_words = urllib.quote('azeite de oliva')
search_category = urllib.quote('azeites')

URL = 'http://busca.paodeacucar.com.br/search?' + \
    'p=Q&lbc=paodeacucar' + \
    '&ts=custom&w=' + search_words + \
    '&isort=price&method=and&view=list&cnt=10' + \
    '&af=categoria:' + search_category


def save(data):
    'Saves page to disk cache'
    file_ = open('./search_results.html', 'w+')
    file_.truncate()
    print >>file_, data


def openURL():
    'Anonymize url request and fetch page'
    ab = anonBrowser()
    ab.anonymize()
    print '[*] Fetching page \n[+] URL: ' + URL
    response = ab.open(URL)
    html = response.read()
#   save(html)
    for cookie in ab.cookie_jar:
        print '[+] Added cookie: ' + str(cookie)
    return html


def getId(text):
    finder = re.compile('^\d+')
    return int(finder.findall(text)[0])


def getURL(text):
    return 'http://www.paodeacucar.com.br' + text


def main():
    try:
        wholehtml = openURL()
        print '\n[+] Returned Products'
        soup = BeautifulSoup(wholehtml)
        prodhtml = soup.findAll("div", "boxProduct")
        for html in prodhtml:
            desc = html.findChild("h3").text
            img = getURL(html.findChild("img").get('src'))
            id_ = getId(html.findChild("footer").get('id'))
            prod = Produto('pda', id_, desc, search_category, None, img)
            print '[.]\t\t Produto: ' + desc
            print json.dumps(vars(prod), sort_keys=True, indent=4)

    except:
        print "[!] Error: ", sys.exc_info()[0]
        pass

if __name__ == '__main__':
        main()
