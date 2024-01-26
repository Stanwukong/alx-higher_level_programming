#!/usr/bin/python3
"""Sends a request to a given URL and displays the response body."""
import sys
import requests as req


if __name__ == "__main__":
    url = sys.argv[1]

    res = req.get(url)
    if res.status_code >= 400:
        print("Error code: {}".format(res.status_code))
    else:
        print(res.text)
