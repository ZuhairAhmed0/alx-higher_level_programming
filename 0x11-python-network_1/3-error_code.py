#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8)
"""
import sys
import urllib.request


if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])

    try:
        with urllib.request.urlopen(req) as response:
            res = response.read().decode('utf8')
        print(res)

    except urllib.error.HTTPError as err:
        print('Error code: {}'.format(err.code))
