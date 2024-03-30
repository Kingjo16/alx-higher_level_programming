#!/usr/bin/python3
"""Script that sends a POST request with the letter as a parameter."""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]

    url = 'http://0.0.0.0:5000/search_user'
    data = {'q': q}

    try:
        resp = requests.post(url, data=data)
        json_data = resp.json()

        if json_data:
            print("[{}] {}".format(json_data.get('id'), json_data.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
