#!/usr/bin/python3
"""Sends a POST request to http://0.0.0.0:5000/search_user with a letter as a parameter."""
import sys
import requests as req


if __name__ == "__main__":
    if len(sys.argv) == 1:
        letter = ""
    else:
        letter = sys.argv[1]
    payload = {"q": letter}

    data = req.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        res = data.json()
        if res == {}:
            print("No result")
        else:
            print("[{}] {}".format(res.get("id"), res.get("name")))
    except ValueError:
        print("Not a valid JSON")
