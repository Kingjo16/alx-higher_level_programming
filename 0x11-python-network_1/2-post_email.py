#!/usr/bin/python3
"""A script that will take a url and siaplay abody of response."""

if __name__ == '__main__':
    import urllib.request
    import urllib.parse
    import sys

    ips = sys.argv[1]
    addr = {"email": sys.argv[2]}
    DATA = urllib.parse.urlencode(addr).encode("ascii")

    given_req = urllib.request.Request(ips, DATA)

    with urllib.request.urlopen(given_req) as resp:
        print(resp.read().decode("utf-8"))
