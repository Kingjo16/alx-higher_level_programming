#!/usr/bin/python3
"""Uses the GitHub API to display your id."""

from requests import get
from sys import argv
from requests.auth import HTTPBasicAuth
import requests

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]

    auth = HTTPBasicAuth(username, password)
    r = requests.get("https://api.github.com/user", auth=auth)
    print(r.json().get("id"))
