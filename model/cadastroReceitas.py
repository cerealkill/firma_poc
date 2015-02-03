#! /usr/bin/python
# -*- coding: utf-8 -*-
from jsonable import Jsonable


class Ingrediente(Jsonable):
    'Ingredientes conhecidos pelo aplicativo'
    def __init__(self, desc, comum, categoria):
        self.desc = desc
        self.comum = comum
        self.categoria = categoria


class Categoria(Jsonable):
    'Palavras chave para filtro de categoria nas pesquisas'
    def __init__(self, nome, origem):
        self.nome = nome
        self.origem = origem
