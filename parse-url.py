import urlparse

url = 'http://bing.com/search?q=good'
res = urlparse.urlparse(url)

print(res)