#!/bin/bash
#  takes in a URL, sends a DELETE request to the URL, and displays the body of the response
curl -Is -X OPTIONS "$1" | grep "allow:" | cut -d ":" -f2
