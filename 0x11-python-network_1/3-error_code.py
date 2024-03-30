#!/usr/bin/python3
"""This is the script that will response to (decoded in utf-8)."""


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

