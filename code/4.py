#!/usr/bin/env python

from urllib import request

url = 'http://www.nhk.or.jp'
charset = 'utf-8'

# you will get HTTP Error 403: Forbidden
response = request.urlopen(url)

binary_code = response.read()
html = binary_code.decode(charset)
print(html)
