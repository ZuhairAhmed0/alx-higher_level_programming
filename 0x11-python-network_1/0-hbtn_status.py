#!/usr/bin/python3
<<<<<<< HEAD
"""  fetches https://intranet.hbtn.io/status  """
=======
"""
Python script that fetches https://alx-intranet.hbtn.io/status
"""
>>>>>>> 4bddcfc8f0f7ac9ea47966c5a4de536755ba26d6
import urllib.request


if __name__ == "__main__":
<<<<<<< HEAD
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    r = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(r)))
    print("\t- content: {}".format(r))
    print("\t- utf8 content: {}".format(r.decode("UTF-8")))
=======
    req = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(req) as response:
        res = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(res)))
        print("\t- content: {}".format(res))
        print("\t- utf8 content: {}".format(res.decode('UTF-8')))
>>>>>>> 4bddcfc8f0f7ac9ea47966c5a4de536755ba26d6
