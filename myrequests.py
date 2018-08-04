import requests

def gets(urls = []):
    for i in urls:
        yield {"response": requests.get(i), "url": i}