#!/usr/bin/env python

# 若找不到对应的url，则增加错误次数，并在错误次数达到阈值后中止查询
import itertools
from . import parseUrl

max_errors = 5

num_errors = 0

for page in itertools.count(1):
    url = 'http://example.webscraping.com/view/-%d' % page
    html = parseUrl.download(url)
    if html is None:
        num_errors += 1
        if num_errors == max_errors:
            break
    else:
        num_errors = 0

