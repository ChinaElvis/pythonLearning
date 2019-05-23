#!/usr/bin/env python
# 从网站地图的xml文件中提取所有url数据

from . import parseUrlBySepcHeader as p
import re


def crawl_sitemap(url):
    # download the sitemap file
    sitemap = p.download(url)
    # extract the sitemap links
    links = re.findall('<loc>(.*?)</loc>', sitemap)
    # download each link
    for link in links:
        html = p.download(link)
        # todo

