#! /usr/bin/python
# -*- coding: utf-8 -*-
from jsonable import Jsonable


class Product(Jsonable):
    'Products from suppliers'
    def __init__(self, supplier, o_id, desc, category, price, img, ingredient):
        self.supplier = supplier
        self.o_id = o_id
        self.desc = desc
        self.category = category
        self.price = price
        self.img = img
        self.ingredient = ingredient
