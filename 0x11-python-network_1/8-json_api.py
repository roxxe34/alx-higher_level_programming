#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST request"""
import sys
import requests

if __name__ == '__main__':
    url = "http://0.0.0.0:5000/search_user"
    letter = sys.argv[1]
    r = requests.post(url, data={'q': letter})
    print(r.text['id'])
    print(r.text['name'])

