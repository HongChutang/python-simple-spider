#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
爬虫启动和调度器
'''

__author__ = 'Evan Hung'

from baike_spider import url_manager, html_downloader, html_parser, html_outputer, spider_cfg


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager() # 初始化url管理器
        self.downloader = html_downloader.HtmlDownloader() # 初始化页面下载器
        self.parser = html_parser.HtmlParser() # 初始化页面解析器
        self.outputer = html_outputer.HtmlOutputer() # 初始化结果页面输出器

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url) # 添加根页面url
        while self.urls.has_new_url(): # 如果url管理器中还有待爬取url则爬取
            try:
                new_url = self.urls.get_new_url() # 获取本次爬取url
                print 'craw %d: %s' % (count, new_url)
                html_cont = self.downloader.download(new_url) # 下载页面
                new_urls, new_data = self.parser.parse(new_url, html_cont) # 解析页面
                self.urls.add_new_urls(new_urls) # 将本次爬取的页面中的url批量存入url管理器
                self.outputer.collect_data(new_data) # 保存本次爬取的页面的目标数据保存

                if count == spider_cfg.config['page_total']: # 如果达到爬取总数要求，则终止爬取任务
                    break
                count = count + 1
            except: # 异常处理
                print 'craw failed'

        self.outputer.output_html()


if __name__ == '__main__':
    root_url = 'https://baike.baidu.com/item/Python/407313'
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
