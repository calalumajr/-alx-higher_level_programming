#!/usr/bin/python3

"""
Uses the GitHub API with Basic Authentication to display your GitHub ID.
"""
import requests
from requests.auth import HTTPBasicAuth
from sys import argv

if __name__ == '__main__':
    url = 'https://api.github.com/users/{}'.format(argv[1])
    r = requests.get(url,
                     auth=HTTPBasicAuth(argv[1], argv[2]))
    print(r.json().get('id'))
