#!/usr/bin/python3
"""list 10 commits (from the most recent to oldest) of the repository rails"""
import sys
import requests

if __name__ == "__main__":
    repository = sys.argv[1]
    owner = sys.argv[2]
    r = requests.get(
        "https://api.github.com/repos/{}/{}/commits".format(
            sys.argv[2], sys.argv[1]))
    data = r.json()
    try:
        for d in range(10):
            print("{}: {}".format(data[d]['sha'],
                                  data[d]["commit"]["author"]["name"]))
    except IndexError:
        pass
