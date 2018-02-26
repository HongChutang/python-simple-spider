# -*- coding: utf-8 -*-

'''
结果页面输出器
'''

__author__ = 'Evan Hung'


class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = open('output.html', 'w')

        fout.write('<html><body>')
        fout.write(u'<h2 style="text-align:center">Python简易爬虫-爬取百科python词条相关的%s个页面下的标题和摘要表</h2>'
                   .encode('utf-8') % len(self.datas))
        fout.write('<table border="1">')
        fout.write(u'<tr><th>序号</th><th>URL</th><th>标题</th><th>摘要</th></tr>'.encode('utf-8'))
        for i, data in enumerate(self.datas):
            fout.write('<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>' %
                       (i + 1, data['url'].encode('utf-8'), data['title'].encode('utf-8'), data['summary'].encode('utf-8')))
        fout.write('</table></body></html>')