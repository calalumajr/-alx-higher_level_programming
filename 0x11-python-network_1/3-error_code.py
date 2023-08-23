#!/usr/bin/python3

"""
Sends a request to a URL, handles HTTP errors, and
Displays the body of the response.
"""
import urllib.error
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
