import requests
from collections import defaultdict
from collections import Counter

url = 'http://www.puzzlers.org/pub/wordlists/unixdict.txt'
words = requests.get(url).content.decode("utf-8").split("\n")

groups = defaultdict(list)

for word in words:
    if word:
        groups[''.join(sorted(word))].append(word)
    
sorted_by_size = sorted(
    (words for words in sets.values()), 
    key=len
)
print(sorted_by_size[-10:])
