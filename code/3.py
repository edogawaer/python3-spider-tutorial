#!/usr/bin/env python

from urllib import request

# a chinese page using GBK charset
url = 'http://www.163.com'

# GB2312<GBK<GB18030
# ''charset = 'GB18030''' also works
charset = 'GBK'

response = request.urlopen(url)
binary_code = response.read()
html = binary_code.decode(charset)
print(html)
