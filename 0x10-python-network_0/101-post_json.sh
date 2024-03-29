#!/bin/bash
# Displays the body to the respons of the JSON POST that is sent by the URL.
curl -s "$1" -d "@$2" -X POST -H "Content-Type: application/json"
