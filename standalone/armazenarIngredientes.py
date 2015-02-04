#! /usr/bin/python
# -*- coding: utf-8 -*-
from cadastroReceitas import Categoria, Ingrediente
from couchdbHandler import Couch


URL = 'http://127.0.0.1:5984'
DATABASE = 'dicionario_ingredientes'


def main():

    i1 = Ingrediente('alface', True,
                     [Categoria('verduras', 'pda')])
    i2 = Ingrediente('rucula', True,
                     [Categoria('verduras', 'pda')])
    i3 = Ingrediente('agriao', True,
                     [Categoria('verduras', 'pda')])
    i4 = Ingrediente('cebola', True,
                     [Categoria('alhoecebola', 'pda')])
    i5 = Ingrediente('alho', True,
                     [Categoria('alhoecebola', 'pda')])
    i6 = Ingrediente('tomate', True,
                     [Categoria('legumes', 'pda')])
    i7 = Ingrediente('batata bolinha', True,
                     [Categoria('legumes', 'pda')])
    i8 = Ingrediente('queijo roquefort', False,
                     [Categoria('queijoselaticinios', 'pda')])
    i9 = Ingrediente('queijo ralado', True,
                     [Categoria('queijoselaticinios', 'pda')])
    i10 = Ingrediente('leite', True,
                      [Categoria('leite', 'pda')])
    i11 = Ingrediente('creme de leite', True,
                      [Categoria('cremedeleite', 'pda')])
    i12 = Ingrediente('manteiga', True,
                      [Categoria('manteigasemargarinas', 'pda')])
    i13 = Ingrediente('margarina', True,
                      [Categoria('manteigasemargarinas', 'pda')])
    i14 = Ingrediente('noz pecan', False,
                      [Categoria('frutassecas', 'pda')])
    i15 = Ingrediente('contra filet', False,
                      [Categoria('bovinos', 'pda')])
    i16 = Ingrediente('azeite de oliva', True,
                      [Categoria('azeites', 'pda')])
    i17 = Ingrediente('chocolate 70% cacau', False,
                      [Categoria('chocolatesebombons', 'pda')])
    i18 = Ingrediente('conhaque', True,
                      [Categoria('whiskiesedestilados', 'pda')])
    i19 = Ingrediente('ovo', True,
                      [Categoria('ovos', 'pda')])
    i20 = Ingrediente('acucar', True,
                      [Categoria('acucareadocantes', 'pda')])
    i21 = Ingrediente('farinha de rosca', False,
                      [Categoria('farinhasefarofas', 'pda')])
    i22 = Ingrediente('tomilho', False,
                      [Categoria('ervaseespeciarias', 'pda'),
                       Categoria('tempero', 'pda'),
                       Categoria('temperosfrescos', 'pda')])
    i23 = Ingrediente('alecrim', False,
                      [Categoria('ervaseespeciarias', 'pda'),
                       Categoria('temperosfrescos', 'pda')])
    i24 = Ingrediente('sal', True,
                      [Categoria('salepimenta', 'pda')])
    i25 = Ingrediente('pimenta cayena', False,
                      [Categoria('salepimenta', 'pda')])
    i26 = Ingrediente('pimenta do reino', True,
                      [Categoria('salepimenta', 'pda')])

    ingredientes = [i1, i2, i3, i4, i5, i6, i7, i8, i9, i10, i11,
                    i12, i13, i14, i15, i16, i17, i18, i19, i20,
                    i21, i22, i23, i24, i25, i26]

    couch = Couch(url_=URL, session_=None)
    couch.del_db(DATABASE)
    db = couch.fetch_db(DATABASE)

    for i in ingredientes:
        print dict(i)
        couch.add_doc(db, dict(i))


if __name__ == '__main__':
    main()
