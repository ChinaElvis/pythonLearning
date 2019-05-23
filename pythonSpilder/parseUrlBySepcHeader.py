#!/usr/bin/env python

# 使用python3的urllib库进行url解析
# 该版本的函数能够捕获异常、重试下载并设置用户代理

import urllib.request


def download(url, user_agent='wswp', num_retries=2):
    print("Downloading:", url)
    headers = {'User-agent': user_agent}
    try:
        # html = urllib.request.urlopen(url).read()
        request = urllib.request.Request(url, headers)
        html = urllib.request.urlopen(request).read()
    except urllib.request.URLError as e:
        print("Download error:", e.reason)
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                # recurisively retry 5xx HTTP errors
                return download(url, num_retries-1)
    return str(html)


print(download("http://www.taobao.com/"))