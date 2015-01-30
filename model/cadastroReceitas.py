# -*- coding: utf-8 -*-
class IterMixin(object):
    def __iter__(self):
        for attr, value in self.__dict__.iteritems():
            if(hasattr(value, '__iter__')):
                yield attr, dict(value)
            else:
                yield attr, value
                

class Ingrediente(IterMixin):
    'Ingredientes conhecidos pelo aplicativo'
    def __init__(self, desc, categoria):
        self.desc = desc
        self.categoria = categoria


class Categoria(IterMixin):
    'Palavras chave para filtro de categoria nas pesquisas'
    def __init__(self, nome, origem):
        self.nome = nome
        self.origem = origem