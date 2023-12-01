#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST request"""
import sys
import requests
import json

if __name__ == '__main__':
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) < 1:
        print("No result")
    else:
        try:
            letter = sys.argv[1]
            r = requests.post(url, data={'q': letter})
            data = r.text
            data_dict = json.loads(data)
            if len(data_dict) == 0:
                print("No result")
            else:
                print("[{}] {}".format(data_dict['id'], data_dict['name']))
        except json.JSONDecodeError:
            print("Not a valid JSON")
