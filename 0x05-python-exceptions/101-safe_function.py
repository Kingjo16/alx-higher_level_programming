#!/usr/bin/python3
from __future__ import print_function
import sys

def safe_function(fct, *args):
    try:
        new_line = fct(*args)
    except Exception as m:
        print("Exception: {}".format(m), file=sys.stderr)
        return None
    else:
        return new_line
