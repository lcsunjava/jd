#coding=utf8
'''
Created on 2017年11月8日
@author: 李超
'''
from scrapy import Item,Field
class JdItem(Item):
    name = Field()
    price = Field()
