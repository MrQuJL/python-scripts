#-*- coding:utf8 -*-


import requests
from lxml import etree
from multiprocessing.dummy import Pool as ThreadPool
import re
import json
import time

# 目标网站：http://tieba.baidu.com/p/3522395718?pn=1
# 目标内容：跟帖用户名，跟帖内容，跟帖时间
# 涉及知识：requests获取网页内容，xPath提取内容，map实现多线程爬虫

# 1.获取网页源码

class UserInfo(object):

    def __init__(self, name, content, time):
        self.name = name
        self.content = content
        self.time = time


def get_code(url):
    temp = requests.get(url)
    return temp.content.decode("utf-8")

# 2.爬取所需内容


def spider(html):
    selector = etree.HTML(html)
    list = selector.xpath('//div[starts-with(@class, "l_post j_l_post l_post_bright")]')
    for each in list:
        # 2.1 跟帖用户名
        obj = json.loads(each.xpath('@data-field')[0])
        print(obj['author']['user_name'])
        # 2.2 跟帖内容
        # msg = each.xpath('div[@class="d_post_content_main"]/cc/div[starts-with(@class, "d_post_content j_d_post_content")]/text()')
        msg = each.xpath('div[@class="d_post_content_main"]/cc')
        # print(msg)
        # 2.3 跟帖时间
        print(obj['content']['date'] + '\n')
    ct = selector.xpath('//div[starts-with(@class, "l_post j_l_post l_post_bright")]/div[@class="d_post_content_main"]/cc/div[@class="d_post_content j_d_post_content  clearfix"]/text()')
    for each in ct:
        print(each)


# 3.输出到文件



#json.loads("text")


pool = ThreadPool(2)
f = open("dsfsf.txt", 'a+')
page = []

# 生成url page

html = get_code("http://tieba.baidu.com/p/3522395718?pn=1")
spider(html)


