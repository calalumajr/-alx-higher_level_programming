#!/usr/bin/python3
"""
Lists 10 commits(from most recent to oldest)
of a repository by a user.
"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("Usage: ./100-github_commits.py repository owner")

    repository = sys.argv[1]
    owner = sys.argv[2]

    url = f'https://api.github.com/repos/{owner}/{repository}/commits'

    response = requests.get(url)

    try:
        data = response.json()
        for commit in data[:10]:
            sha = commit['sha']
            author = commit['commit']['author']['name']
            print(f"{sha}: {author}")
    except ValueError:
        print("Invalid response from GitHub API")
