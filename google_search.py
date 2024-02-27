from googlesearch import search

def google_search(query: str):
    return search(query, num=10, stop=10, pause=2)
