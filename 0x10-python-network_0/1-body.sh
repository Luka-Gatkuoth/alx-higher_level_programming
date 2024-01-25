#!/bin/bash
# A Bash scripts that take in a URL, send a GET request and display only the  body of a 200 status code response
curl -Ls "$1"
