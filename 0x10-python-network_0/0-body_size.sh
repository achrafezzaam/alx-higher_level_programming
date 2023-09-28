#!/bin/bash
# Get the Content-Length of a given URL
curl -s "$1" | wc -c 
