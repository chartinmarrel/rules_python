import requests

def hello():
    requests.get("http://www.google.fr")
    return 'hello'