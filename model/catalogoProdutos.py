#! /usr/bin/python
# -*- coding: utf-8 -*-
from jsonable import Jsonable


class Produto(Jsonable):
    'Produtos extraídos dos sites'
    def __init__(self, origem, o_id, desc, categoria, preco, img, ingrediente):
        self.origem = origem
        self.o_id = o_id
        self.desc = desc
        self.categoria = categoria
        self.preco = preco
        self.img = img
        self.ingrediente = ingrediente
