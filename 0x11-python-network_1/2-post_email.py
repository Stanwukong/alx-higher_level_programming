#!/usr/bin/python3
"""Sends a POST request to specified URL using email
and displays the body of the resposnse."""
import urllib.parse
import urllib.request
import sys


if __name__ == "__main__":
    URL = sys.argv[1]
    EMAIL = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(EMAIL).encode("ascii")

    req = urllib.request.Request(URL, data)
    with urllib.request.urlopen(req) as res:
        print(res.read().decode("utf-8"))        
