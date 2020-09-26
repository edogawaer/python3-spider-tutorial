#!/usr/bin/env python

from urllib import request

url = 'https://www.fang.com'
charset = 'GB18030'
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'zh-CN, zh; q=0.9',
    'Accept-Encoding': 'gzip, deflate',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
}
req = request.Request(url, headers=headers)
response = request.urlopen(req)
binary_code = response.read()

# you will get a UnicodeDecodeError: 'gb18030' codec can't decode byte 0x8b ...
# because the binary code is compressed.
html = binary_code.decode(charset)

print(html)
