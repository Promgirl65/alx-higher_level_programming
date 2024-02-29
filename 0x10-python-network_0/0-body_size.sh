#!/bin/bash
# Bash script that takes in a URL using curl
curl -s "$1" | wc -c
