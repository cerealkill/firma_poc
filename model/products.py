#! /usr/bin/python
# -*- coding: utf-8 -*-
from jsonable import Jsonable

class ProductId(Jsonable):
    'Products identifier'
    def __init__(self, supplier, o_id):
        self.supplier = supplier
        self.o_id = o_id

class Product(Jsonable):
    'Products from suppliers'
    def __init__(self, p_id, desc, category, price, img, ingredient):
        self.p_id = p_id
        self.desc = desc
        self.category = category
        self.price = price
        self.img = img
        self.ingredient = ingredient


class Ingredient(Jsonable):
    'Known recipe ingredient'
    def __init__(self, desc, common, category):
        self.desc = desc
        self.commom = common
        self.category = category


class Category(Jsonable):
    'Key words to filter search results'
    def __init__(self, name, source):
        self.name = name
        self.source = source