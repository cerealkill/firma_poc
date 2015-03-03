#! /usr/bin/python
# -*- coding: utf-8 -*-
import datetime
import decimal
import json

class Jsonable(object):
    def __iter__(self):
        for attr, value in self.__dict__.iteritems():
            if isinstance(value, datetime.datetime):
                iso = value.isoformat()
                yield attr, iso
            elif isinstance(value, decimal.Decimal):
                yield attr, str(value)
            elif(hasattr(value, '__iter__')):
                if(hasattr(value, 'pop')):
                    a = []
                    for subval in value:
                        if(hasattr(subval, '__iter__')):
                            a.append(dict(subval))
                        else:
                            a.append(subval)
                    yield attr, a
                else:
                    yield attr, dict(value)
            else:
                yield attr, value
    
    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)