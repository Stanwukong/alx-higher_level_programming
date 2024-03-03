#!/usr/bin/python3
"""Sends a POST request to specified URL using email
and displays the body of the resposnse."""
import urllib
import sys


if __name__ == "__main__":
    URL = sys.argv[1]
    EMAIL = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(EMAIL).encode("ascii")

    req = urllib.requests.Request(URL, data)
    with urllib.requests.urlopen(req) as res:
        print(res.read().decode("utf-8"))        
