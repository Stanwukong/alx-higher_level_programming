#!/usr/bin/python3
"""Displays the X-Request-Id header variable of a request to a given URL."""

import sys
import requests as req


if __name__ == "__main__":
    url = sys.argv[1]
    res = req.get(url)
    print(res.headers.get("X-Request-Id"))
