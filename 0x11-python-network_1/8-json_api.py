#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST request"""
import sys
import requests

if __name__ == '__main__':
    url = "http://0.0.0.0:5000/search_user"
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    r = requests.post(url, data={'q': letter})
    try:
        data = r.json()
        if len(data) == 0:
            print("No result")
        else:
            print("[{}] {}".format(data['id'], data['name']))
    except ValueError:
        print("Not a valid JSON")
