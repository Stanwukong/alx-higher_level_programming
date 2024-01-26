#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status."""
import requests as req


if __name__ == "__main__":
    res = req.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(res.text)))
    print("\t- content: {}".format(res.text))
