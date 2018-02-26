# -*- coding: utf-8 -*-

'''
页面下载器
'''

__author__ = 'Evan Hung'


import urllib2


class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return

        response = urllib2.urlopen(url)

        if response.getcode() != 200:
            return

        return response.read()
