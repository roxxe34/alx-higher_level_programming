#!/usr/bin/python3
""" Python script that takes your GitHub credentials to display your id"""
import requests
import sys
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    auths = HTTPBasicAuth(username, password)
    r = requests.get("https://api.github.com/user", auth=auths)
    print(r.json().get("id"))
