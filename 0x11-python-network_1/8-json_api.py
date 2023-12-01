#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST request"""
import sys
import requests

if __name__ == '__main__':
    url = sys.argv[1]
    letter = sys.argv[2]
    r = requests.post(url, data={'q': letter})
    print(r.text)
