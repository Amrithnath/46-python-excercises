import requests
from itertools import zip_longest

url = 'http://www.puzzlers.org/pub/wordlists/unixdict.txt'
words = set(word for word in requests.get(url).content.decode("utf-8").split("\n") if word)

for word in words:
    alternades = list(zip(*zip_longest(*[iter(word)]*2)))
    first = ''.join(letter for letter in alternades[0] if letter)
    second = ''.join(letter for letter in alternades[1] if letter)
    
    if first in words and second in words:
        print('"{}": makes "{}" and "{}"'.format(word, first, second))
