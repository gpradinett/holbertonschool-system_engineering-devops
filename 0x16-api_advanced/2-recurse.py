#!/usr/bin/python3
"""
Write a recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit. If no results
are found for the given subreddit, the function should return None.
Hint: The Reddit API uses pagination for separating pages of responses.
Requirements:
- Prototype: def recurse(subreddit, hot_list=[])
- Note: You may change the prototype, but it must be able to be called with
just a subreddit supplied. AKA you can add a counter, but it must work without
supplying a starting value in the main.
- If not a valid subreddit, return None.
- NOTE: Invalid subreddits may return a redirect to search results. Ensure that
you are not following redirects.
Your code will NOT pass if you are using a loop and not recursively calling the
function! This /can/ be done with a loop but the point is to use a recursive
function. :)
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    recursive function that queries the Reddit API and returns
    a list containing the titles of all hot articles for a given
    subreddit
    """
    try:
        url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

        headers = requests.utils.default_headers()

        # Seteamos el User-Agent para no tener problemas de "too many requests"
        headers.update({'User-Agent': 'My User Agent 1.0'})

        # Hacemos una request de la url indicada arriba con el metodo GET
        res = requests.get(url, headers=headers, params={'after': after},
                           allow_redirects=False)

        # Pasar datos a JSON para obtener un diccionario de python y poder
        # trabajar con los datos en python
        res_json = res.json()

        child = res_json['data']['children']

        # Se hace un append de cada dato dentro de child en la lista a retornar
        for title in child:
            hot_list.append(title['data']['title'])

        # Con after se itera por todos los datos
        after = res_json['data']['after']

        # Mientras que haya paginas para recorrer se sigue con la recursion
        if after is not None:
            recurse(subreddit, hot_list, after)

        # Si no se entra en el if de arriba y se retorna la hot_list es por
        # que se cumplio la condicion base y se sale de la recursion
        return hot_list

    except Exception:
        # If not a valid subreddit, return None.
        return None
