# -*- coding: utf-8 -*-
'''
url管理器
'''

__author__ = 'Evan Hung'


class UrlManager(object):
    def __init__(self): # 将待爬取和已爬取url定义为无序不重复集合
        self.new_urls = set()
        self.old_urls = set()

    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls: # 如果是全新的url，则添加
            self.new_urls.add(url)

    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def has_new_url(self):
        return not len(self.new_urls) == 0

    def get_new_url(self): # 从待爬取集合中取出并添加到已爬取集合
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url
