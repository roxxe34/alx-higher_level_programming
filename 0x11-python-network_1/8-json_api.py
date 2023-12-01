#!/usr/bin/python3
"""Sends a POST request to http://0.0.0.0:5000/search_user with a given letter.

Usage: ./8-json_api.py <letter>
  - The letter is sent as the value of the variable `q`.
  - If no letter is provided, sends `q=""`.
"""
import sys
import requests
import json

if __name__ == '__main__':
    url = "http://0.0.0.0:5000/search_user"
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    r = requests.post(url, data={'q': letter})
    data = r.text
    try:
        data_dict = json.loads(data)
        if len(data_dict) == 0:
            print("No result")
        else:
            print("[{}] {}".format(data_dict['id'], data_dict['name']))
    except json.JSONDecodeError:
        print("Not a valid JSON")
