import urllib
webpage = urllib.request.urlopen('http://www.python.org')
text = webpage.read()
print(text)

