#!/usr/bin/python3
"""Sends a POST request to a given URL with a given email."""
import sys
import requests as req


if __name__ == "__main__":
    url = sys.argv[1]
    val = {"email": sys.argv[2]}

    res = req.post(url, data=val)
    print(res.text)
