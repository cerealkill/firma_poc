#! /usr/bin/python
# -*- coding: utf-8 -*-
class Jsonable(object):
    def __iter__(self):
        for attr, value in self.__dict__.iteritems():
            if(hasattr(value, '__iter__')):
                a = []
                if(hasattr(value, 'append')):
                    for subval in value:
                        a.append(dict(subval))
                    yield attr, a
                else:
                    a.append(dict(value))
                    yield attr, a
            else:
                yield attr, value

