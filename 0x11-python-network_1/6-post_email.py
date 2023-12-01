#!/usr/bin/python3
""" Python script that takes in a URL and an email,sends a POST request"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    r = requests.post(url, data={'email': email})
    print(r.text)
