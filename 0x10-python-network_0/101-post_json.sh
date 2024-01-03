#!/bin/bash
#Bash script that makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with a message
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
