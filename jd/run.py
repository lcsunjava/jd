#coding=utf8
'''
Created on 2017年11月8日
@author: 李超
'''
from scrapy import cmdline
from jd.spiders.JdSpider import JdSpider

if __name__=="__main__":
    JdSpider.start_urls = ['http://search.jd.com/Search?keyword=%E6%98%BE%E7%A4%BA%E5%99%A8&enc=utf-8&suggest=1.def.0.V19&wq=%E6%98%BE&pvid=8b1a22e858584fea9ef1a7c20181db7c']
    cmdline.execute("scrapy crawl jd".split())