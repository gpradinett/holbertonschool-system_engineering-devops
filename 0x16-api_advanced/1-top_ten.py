#!/usr/bin/python3
"""
Write a function that queries the Reddit API and prints the titles of the first
10 hot posts listed for a given subreddit.
Requirements:
- Prototype: def top_ten(subreddit)
- If not a valid subreddit, print None.
- NOTE: Invalid subreddits may return a redirect to search results. Ensure that
you are not following redirects.
How to set User-Agent:
https://stackoverflow.com/questions/10606133/%20sending-user-agent-using-
requests-library-in-python
Info request module python: https://realpython.com/python-requests/
"""

import requests


def top_ten(subreddit):
    """
    Return the first 10 hot posts listed in the subreddit passed as argument
    """
    # Esta va a ser la URL a la que vamos a hacer una request, subreddit va
    # a ser el "tema" que se pase como argumento en linea, usamos
    # "query string" para pasarle un limit a la request de 10 resultados
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)

    # Seteamos el User-Agent para no tener problemas de "too many requests"
    headers = {'User-Agent': 'My User Agent 1.0'}

    # Hacemos una request de la url indicada arriba con el metodo GET
    data = requests.get(url, headers=headers, allow_redirects=False)

    if data.status_code == 404:
        print("None")

    else:
        for result in data.json().get("data").get("children"):
            print("{}".format(result.get("data").get("title")))
