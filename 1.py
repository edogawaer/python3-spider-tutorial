#!/usr/bin/env python

# request module of urllib should be imported to retrieve a webpage
# ''import urllib.request'' also works
# but you should use urllib.request instead of request in the following codes
from urllib import request

# webpage to be retrieved
url = 'http://www.python.org/'

# requesting the page and geting a response
response = request.urlopen(url)

# reading binary code of the page from the response
binary_code = response.read()

# decoding binary code to readble HTML text
html = binary_code.decode()

# printing HTML text
print(html)
