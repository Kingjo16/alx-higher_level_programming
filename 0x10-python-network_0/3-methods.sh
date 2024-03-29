#!/bin/bash
# Take the URL and Displays all HTTP methods the server will accept.
curl -s -I "${1}" | grep "^Allow: .*" | cut -d " " -f 2-
