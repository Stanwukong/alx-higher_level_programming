#!/usr/bin/python3
"""Fetches a website."""
import urllib

if __name__ == "__main__":
    page = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(page) as response:
        html = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))
