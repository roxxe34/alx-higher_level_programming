#!/usr/bin/python3
"""list 10 commits (from the most recent to oldest) of the repository rails"""
import sys
import requests

if __name__ == "__main__":
    repository = sys.argv[1]
    owner = sys.argv[2]
    r = requests.get(
        f"https://api.github.com/repos/{sys.argv[1]}/{sys.argv[2]}/commits")
    data = r.json()
    for d in range(10):
        print("{}: {}".format(data[d]['sha'],
                              data[d]["commit"]["author"]["name"]))