#!/usr/bin/python3
"""Uses the GitHub API to display a GitHub ID based on provided credentials."""
import sys
import requests as req
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    res = req.get("https://api.github.com/user", auth=auth)
    print(res.json().get("id"))
