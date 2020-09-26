#!/usr/bin/env python

from urllib import request

url = 'http://www.nhk.or.jp'
charset = 'utf-8'

# constructing HTTP headers information
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'zh-CN, zh; q=0.9',
    'Accept-Encoding': 'gzip, deflate',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
}

# constructing HTTP request with HTTP headers
req = request.Request(url, headers=headers)

# mimicing a webbrowser to request the page
response = request.urlopen(req)

binary_code = response.read()
html = binary_code.decode(charset)
print(html)
