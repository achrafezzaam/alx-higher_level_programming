#!/bin/bash
# Get the Content-Length of a given URL
curl -sI "$1" | grep "content-length" | cut -d " " -f 2-
