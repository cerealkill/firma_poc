#! /usr/bin/python
# -*- coding: utf-8 -*-
from recipes import *
from products import ProductId
from cozy_couch import Couch


URL = 'http://127.0.0.1:5984'
DATABASE = 'recipes'


def main():

    i1 = Ingredient('1 unidade', 'alface') #alface
    i2 = Ingredient('1 unidade', 'rucula') #rucula
    i3 = Ingredient('1 unidade', 'agriao') #agriao
    i4 = Ingredient('70 gramas', 'queijo roquefort') #roquefort
    i5 = Ingredient('80 ml', 'creme de leite') #creme de leite
    i6 = Ingredient('50 gramas', 'noz pecan') #noz pecan
    
    p1 = ProductId('pda', '134405')
    p2 = ProductId('pda', '292549')
    p3 = ProductId('pda', '19195')
    p4 = ProductId('pda', '311053')
    
    s1 = Step(0, '5 min', 'Higienize', [i1, i2, i3], 'Higienize as folhas e retire os talos.')
    s2 = Step(1, '3 min', ['coloque', 'deixe', 'derreter'], [i4, i5], 'Em uma panela coloquei o queijo e o creme de leite e deixe derreter o queijo.')
    s3 = Step(2, '4 min', ['Monte', 'quebre', 'despeje'], [0, 1], 'Monte as folhas e com as mãos quebre as nozes por cima das folhas despeje o molho morno sobre as folhas.'.decode('utf-8'))
    s4 = Step(3, '', 'Sirva', 2, 'Sirva em seguida.')
    
    src1 = Source('self', 'salada-especial-do-rafa')
    
    r1 = Recipe('Salada especial do Rafa', [i1, i2, i3, i4 ,i5, i6], [s1, s2, s3, s4], [p1, p2, p3, p4], src1)

    couch = Couch(url_=URL, session_=None)
    couch.del_db(DATABASE)
    db = couch.fetch_db(DATABASE)

    print dict(r1)
    couch.add_doc(db, dict(r1))
    
    map_function = "function(doc) {if(doc.source.url == \""+ r1.source.url \
        +"\") emit(\"recipe\", {\"name\": doc.name, \"steps\": doc.steps, \"ingredients\": doc.ingredients, \"products\": doc.products}); }"
    views = {}
    views[r1.source.url] = {'map': map_function} 
    
    view_doc = couch.create_view_doc('by_url', views)
    couch.add_view_doc(db, view_doc)


if __name__ == '__main__':
    main()