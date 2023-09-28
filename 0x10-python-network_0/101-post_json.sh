#!/bin/bash
# a Bash script that sends POST request and displays the body of the response
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
