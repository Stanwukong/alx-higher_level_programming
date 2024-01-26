#!/usr/bin/python3
"""Sends a POST request and displays the body of the response."""


import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":
    url = sys.argv[1]
    val = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(val).encode("ascii")

    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as res:
        body = res.read().decode("utf-8")
        print(body)
