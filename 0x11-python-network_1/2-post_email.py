#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL and displays"""
import urllib.parse
import urllib.request
import sys

url = sys.argv[1]
value = sys.argv[2]

data = urllib.parse.urlencode(tuple(value))
data = data.encode("utf-8")
req = urllib.request.Request(url, data)
with urllib.request.urlopen(req) as response:
    the_page = response.read()
