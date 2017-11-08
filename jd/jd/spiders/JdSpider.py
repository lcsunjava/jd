#coding=utf8
'''
Created on 2017年11月8日
@author: 李超
'''
import scrapy
from jd.items import JdItem
class JdSpider(scrapy.Spider):
    name = 'jd'
    allowed_domains = ['search.jd']
    start_urls = [
            'http://search.jd.com/Search?keyword=%E6%98%BE%E7%A4%BA%E5%99%A8&enc=utf-8&suggest=1.def.0.V19&wq=%E6%98%BE&pvid=8b1a22e858584fea9ef1a7c20181db7c'
        ]
    
    def parse(self,response):
        for sel in response.xpath('//ul[@class="gl-warp clearfix"]/li/div[@class="gl-i-wrap"]'):
            item = JdItem()
            item['name']=sel.xpath('.//div[@class="p-name p-name-type-2"]//em/text()').extract()
            item['price']=sel.xpath('.//div[@class="p-price"]/strong/i/text()').extract()
            yield item
    
    
    
    
    
    
    
    
    
    