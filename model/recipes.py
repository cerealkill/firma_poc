#! /usr/bin/python
# -*- coding: utf-8 -*-
from jsonable import Jsonable


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
