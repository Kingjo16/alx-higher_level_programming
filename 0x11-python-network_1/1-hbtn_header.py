#!/usr/bin/python3
"""A script that takes a URL and sisplay a Value of the X-request."""


if __name__ == "__main__":
    import sys
    import urllib.request

    with urllib.request.urlopen(sys.argv[1]) as res:
        print(res.headers["X-Request-Id"])
