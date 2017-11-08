#coding=utf8
'''
Created on 2017年11月8日
@author: 李超
'''
from openpyxl import Workbook

class JdPipeline(object):
    def __init__(self):
        self.wb = Workbook()
        self.ws = self.wb.active
        self.ws.title = 'jd'
            
    def process_item(self,item,spider):
        self.ws.append([str(item["name"]).decode('unicode-escape'),str(item["price"]).decode('unicode-escape')])
        self.wb.save("jd.xlsx")
        return item
            
