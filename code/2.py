#!/usr/bin/env python

from urllib import request

# a chinese page using GBK charset
url = 'http://www.163.com'

response = request.urlopen(url)
binary_code = response.read()

# you will receive a error
# 'utf-8' codec can't decode byte ...
html = binary_code.decode()

print(html)
