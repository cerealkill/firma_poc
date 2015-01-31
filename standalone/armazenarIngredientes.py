# -*- coding: utf-8 -*-
import json

from cadastroReceitas import Categoria, Ingrediente
from couchdbHandler import Couch


URL = 'http://127.0.0.1:5984'
DATABASE = 'dicionario_ingredientes'


class ComplexEncoder(json.JSONEncoder):
    'JSON encoder override'
    def default(self, obj):
        if hasattr(obj, 'js'):
            return obj.js()
        else:
            return json.JSONEncoder.default(self, obj)


def main():
    i1 = Ingrediente('alface', True, Categoria('verduras', 'pda'))
    i2 = Ingrediente('rúcula', True, Categoria('verduras', 'pda'))
    i3 = Ingrediente('agrião', True, Categoria('verduras', 'pda'))
    i4 = Ingrediente('cebola', True, Categoria('alhoecebola', 'pda'))
    i5 = Ingrediente('alho', True, Categoria('alhoecebola', 'pda'))
    i6 = Ingrediente('tomate', True, Categoria('legumes', 'pda'))
    i7 = Ingrediente('batata bolinha', True, Categoria('legumes', 'pda'))
    i8 = Ingrediente('queijo roquefort', False, Categoria('queijoselaticinios', 'pda'))
    i9 = Ingrediente('queijo ralado', True, Categoria('queijoselaticinios', 'pda'))
    i10 = Ingrediente('leite', True, Categoria('leite', 'pda'))
    i11 = Ingrediente('creme de leite', True, Categoria('cremedeleite', 'pda'))
    i12 = Ingrediente('manteiga', True, Categoria('manteigasemargarinas', 'pda'))
    i13 = Ingrediente('margarina', True, Categoria('manteigasemargarinas', 'pda'))
    i14 = Ingrediente('noz pecan', False, Categoria('frutassecas', 'pda'))
    i15 = Ingrediente('contra filet', False, Categoria('bovinos', 'pda'))
    i16 = Ingrediente('azeite de oliva', True, Categoria('azeites', 'pda'))
    i17 = Ingrediente('chocolate 70% cacau', False, Categoria('chocolatesebombons', 'pda'))
    i18 = Ingrediente('conhaque', True, Categoria('whiskiesedestilados', 'pda'))
    i19 = Ingrediente('ovo', True, Categoria('ovos', 'pda'))
    i20 = Ingrediente('açúcar', True, Categoria('acucareadocantes', 'pda'))
    i21 = Ingrediente('farinha de rosca', False, Categoria('farinhasefarofas', 'pda'))
    i22 = Ingrediente('tomilho', False, [Categoria('ervaseespeciarias', 'pda'), Categoria('tempero', 'pda'), Categoria('temperosfrescos', 'pda')])
    i23 = Ingrediente('alecrim', False, [Categoria('ervaseespeciarias', 'pda'), Categoria('temperosfrescos', 'pda')])
    i24 = Ingrediente('sal', True, Categoria('salepimenta', 'pda'))
    i25 = Ingrediente('pimenta cayena', False, Categoria('salepimenta', 'pda'))
    i26 = Ingrediente('pimenta do reino', True, Categoria('salepimenta', 'pda'))
   
    ingredientes = [i1, i2, i3, i4, i5, i6, i7, i8, i9, i10, i11, i12, i13, i14, i15, i16, i17, i18, i19, i20, i21, i22, i23, i24, i25, i26]    
    #print json.dumps(i1.js(), cls=ComplexEncoder, sort_keys=True, indent=4)
    for i in ingredientes:
        print json.dumps(dict(i), sort_keys=True, indent=4)
"""
    couch = Couch(url_=URL, session_=None)
    couch.print_dbs()
    db = couch.fetch_db(DATABASE)
    i1_doc = couch.add_doc(db, dict(i1))
    i1_doc['desc'] = 'alface-crespa'
    couch.update_doc(db, i1_doc)
    couch.del_doc(db, i1_doc)"""


if __name__ == '__main__':
    main()


"""
1 unidade de alface
1 unidade de rúcula
1 unidade de agrião
70gr de roquefort
80ml de creeme de leite
 50gr  Noz pecan
 500gr de contra filet (peça)
400 gr de batata bolinha
1 unidDe de agrião
3 dentes de alho
2 ramos de tomilho
4 ramos de alecrim
150 ml de azeite
150 de manteiga
300 gr de chocolate 70% cacau
150ml de creme de leite
50 ml de conhaque
3 ovos
50 gr de açúcar
 02 e ½ xícaras (chá) de batata amassada
02 ovos com as gemas separadas
01 xícara (chá) de queijo ralado
Sal e pimenta a gosto
1 cebola grande (a maior que encontrar)
1 litro de leite
2 ovos
500g de farinha de rosca
2 colheres de sobremesa de sal
2 colheres de sobremesa de pimenta caiena
2 colheres de sobremesa de pimenta do reino
2 colheres de sobremesa de tomilho
"""