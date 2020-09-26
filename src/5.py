#!/usr/bin/env python

from urllib import request

url = 'http://www.nhk.or.jp'
charset = 'utf-8'

# constructing HTTP headers information
# seting User-Agent to Chrome
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
}

# constructing HTTP request with HTTP headers
req = request.Request(url, headers=headers)

# mimicing Chrome to request the page
response = request.urlopen(req)

binary_code = response.read()
html = binary_code.decode(charset)
print(html)
