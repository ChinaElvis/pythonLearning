#!/usr/bin/env python

# 检测某网站使用的技术
import builtwith
import whois
print(builtwith.parse("http://www.taobao.com"))
print(whois.whois('www.baidu.com'))

