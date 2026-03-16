#!/usr/bin/python3
import sys
from urllib.request import urlopen

url = sys.argv[1]

with urlopen(url) as response:
    print(response.headers.get('X-Request-Id'))
