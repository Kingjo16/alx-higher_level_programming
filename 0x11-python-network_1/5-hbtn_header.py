#!/usr/bin/python3
"""A script that send a url variable of X-request abd get an email."""

if __name__ == '__main__':
    from requests import get
    from sys import argv

    res = get(argv[1])
    print(res.headers.get('X-Request-Id'))
