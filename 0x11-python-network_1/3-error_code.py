#!/usr/bin/python3
"""
A script that takes in a URL and sends a request to the URL
and displays the body of the response (decoded in utf-8).
"""


if __name__ == "__main__":
    import urllib.request
    import urllib.error
    import sys


    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as resp:
            print(resp.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.status))

