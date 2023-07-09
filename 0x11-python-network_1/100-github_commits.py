#!/usr/bin/python3
"""
Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
import requests
import sys

if __name__ == '__main__':

    res = requests.get('https://api.github.com/repos/{}/{}/commits'
                       .format(sys.argv[1], sys.argv[2]))

    counter = 0

    for commit in sorted(res.json, key lambda c: c.get("commit")
                         .get("author").get("date"), reverse=True):
        print(commit.get("sha") + ": ", end="")
        print(commit.get("commit").get("author").get("name"))
        counter += 1

        if counter == 10:
            break
