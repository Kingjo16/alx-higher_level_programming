#!/usr/bin/python3
"""Script that will Fetches https://alx-intranet.hbtn.io/status."""
import urllib.request


if __name__ == "__main__":
    req = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(req) as responser:
        con_body = responser.read()
        print("Body response:")
        print("\t- type: {}".format(type(con_body)))
        print("\t- content: {}".format(con_body))
        print("\t- utf8 content: {}".format(con_body.decode("utf-8")))
