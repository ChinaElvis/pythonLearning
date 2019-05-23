#!/usr/bin/env python

# 使用python3的urllib库进行url解析

import urllib.request


def download(url, num_retries=2):
    print("Downloading:", url)
    try:
        html = urllib.request.urlopen(url).read()
    except urllib.request.URLError as e:
        print("Download error:", e.reason)
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                # recurisively retry 5xx HTTP errors
                return download(url, num_retries-1)
    return str(html)


print(download("http://www.taobao.com/"))


