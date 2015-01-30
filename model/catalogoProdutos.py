# -*- coding: utf-8 -*-
class Produto():
    'Produtos extraídos dos sites'
    def __init__(self, origem, id_, desc, categoria, preco, img):
        self.origem = origem
        self.id_ = id_
        self.desc = desc
        self.categoria = categoria
        self.preco = preco
        self.img = img

    def js(self):
        return dict(origem=self.origem, id_=self.id_, desc=self.desc,
                    categoria=self.categoria, preco=self.preco, img=self.img)
