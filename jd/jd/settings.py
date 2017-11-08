#coding=utf8
'''
Created on 2017年11月8日
@author: 李超
'''
BOT_NAME = 'jd'
SPIDER_MODULES = ['jd.spiders']
NEWSPIDER_MODULE='jd.spiders'

ITEM_PIPELINES = {'jd.pipelines.JdPipeline':300}

