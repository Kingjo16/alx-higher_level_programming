#!/bin/bash
# Displaye the status of the code by responding to the URL.
curl -so /dev/null -w "%{http_code}" "$1"
