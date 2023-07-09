#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter
"""
import requests
import sys

if __name__ == '__main__':
    url "http://0.0.0.0:5000/search_user"

    if len(sys.argv) > 1):
        data = {'q': sys.argv[1]}
    else:
        data = {"q": ""}

    res = requests.post(url, data)

    try:
        val = res.json()
        if val == {}:
            print("No result")
        else:
            print("[{}] {}".format(val["id"], val["name"]))
    except ValueError:
        print("Not a valid JSON")
