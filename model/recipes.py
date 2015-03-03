#! /usr/bin/python
# -*- coding: utf-8 -*-
from jsonable import Jsonable


class Recipe(Jsonable):
    'Recipe definition'
    def __init__(self, name, ingredients, steps, products, source):
        self.name = name
        self.ingredients = ingredients
        self.steps = steps
        self.products = products
        self.source = source


class Ingredient(Jsonable):
    'Recipe ingredient'
    def __init__(self, amount, name):
        self.amount = amount
        self.name = name


class Step(Jsonable):
    'Recipe step'
    def __init__(self, index, time, verb, ingredients, text):
        self.index = index
        self.time = time
        self.verb = verb
        self.ingredients = ingredients
        self.text = text


class Source(Jsonable):        
    'Recipe source'
    def __init__(self, name, url):
        self.name = name
        self.url = url    