# -*- coding: utf-8 -*-

'''
页面解析器
'''

__author__ = 'Evan Hung'


import urlparse

import re
from bs4 import BeautifulSoup


class HtmlParser(object):
    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data

    def _get_new_urls(self, page_url, soup):
        new_urls = set()

        # 搜索href属性为/item/***格式的所有链接标签
        links = soup.find_all('a', href=re.compile(r'/item/\w+'))
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url, new_url) # 合并为完整url
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        res_data = {}

        # url
        res_data['url'] = page_url

        # 搜索标题标签 规则为<dd class ="lemmaWgt-lemmaTitle-title"><h1> title text </h1>
        title_node = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
        if title_node:
            res_data['title'] = title_node.get_text()
        else:
            res_data['title'] = ''

        # 搜索摘要标签 规则为<div class ="lemma-summary"> summary content </div>
        summary_node = soup.find('div', class_='lemma-summary')
        if summary_node:
            res_data['summary'] = summary_node.get_text()
        else:
            res_data['summary'] = ''

        return res_data
