#!/bin/bash
# Bash script that takes in a URL, sends a request to that URL, and displays the size of BODY
curl -s "$1" | wc -c
