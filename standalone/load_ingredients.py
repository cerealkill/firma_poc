#! /usr/bin/python
# -*- coding: utf-8 -*-
from products import Category, Ingredient
from cozy_couch import Couch


URL = 'https://firma.iriscouch.com'
DATABASE = 'ingredients'


def main():

    i1 = Ingredient('alface', True,
                     [Category('verduras', 'pda')])
    i2 = Ingredient('rucula', True,
                     [Category('verduras', 'pda')])
    i3 = Ingredient('agriao', True,
                     [Category('verduras', 'pda')])
    i4 = Ingredient('cebola', True,
                     [Category('alhoecebola', 'pda')])
    i5 = Ingredient('alho', True,
                     [Category('alhoecebola', 'pda')])
    i6 = Ingredient('tomate', True,
                     [Category('legumes', 'pda')])
    i7 = Ingredient('batata bolinha', True,
                     [Category('legumes', 'pda')])
    i8 = Ingredient('queijo roquefort', False,
                     [Category('queijoselaticinios', 'pda')])
    i9 = Ingredient('queijo ralado', True,
                     [Category('queijoselaticinios', 'pda')])
    i10 = Ingredient('leite', True,
                      [Category('leite', 'pda')])
    i11 = Ingredient('creme de leite', True,
                      [Category('cremedeleite', 'pda')])
    i12 = Ingredient('manteiga', True,
                      [Category('manteigasemargarinas', 'pda')])
    i13 = Ingredient('margarina', True,
                      [Category('manteigasemargarinas', 'pda')])
    i14 = Ingredient('noz pecan', False,
                      [Category('frutassecas', 'pda')])
    i15 = Ingredient('contra filet', False,
                      [Category('bovinos', 'pda')])
    i16 = Ingredient('azeite de oliva', True,
                      [Category('azeites', 'pda')])
    i17 = Ingredient('chocolate 70% cacau', False,
                      [Category('chocolatesebombons', 'pda')])
    i18 = Ingredient('conhaque', True,
                      [Category('whiskiesedestilados', 'pda')])
    i19 = Ingredient('ovo', True,
                      [Category('ovos', 'pda')])
    i20 = Ingredient('acucar', True,
                      [Category('acucareadocantes', 'pda')])
    i21 = Ingredient('farinha de rosca', False,
                      [Category('farinhasefarofas', 'pda')])
    i22 = Ingredient('tomilho', False,
                      [Category('ervaseespeciarias', 'pda'),
                       Category('tempero', 'pda'),
                       Category('temperosfrescos', 'pda')])
    i23 = Ingredient('alecrim', False,
                      [Category('ervaseespeciarias', 'pda'),
                       Category('temperosfrescos', 'pda')])
    i24 = Ingredient('sal', True,
                      [Category('salepimenta', 'pda')])
    i25 = Ingredient('pimenta cayena', False,
                      [Category('salepimenta', 'pda')])
    i26 = Ingredient('pimenta do reino', True,
                      [Category('salepimenta', 'pda')])

    ingredients = [i1, i2, i3, i4, i5, i6, i7, i8, i9, i10, i11,
                    i12, i13, i14, i15, i16, i17, i18, i19, i20,
                    i21, i22, i23, i24, i25, i26]

    couch = Couch(url_=URL, session_=None)
    couch.del_db(DATABASE)
    db = couch.fetch_db(DATABASE)

    for i in ingredients:
        print dict(i)
        couch.add_doc(db, dict(i))


if __name__ == '__main__':
    main()