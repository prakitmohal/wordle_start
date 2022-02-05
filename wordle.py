import urllib.request
from collections import Counter

# This appears to have the list of all the wordle answers, but you can use any source of words
url = "https://gist.githubusercontent.com/cfreshman/a03ef2cba789d8cf00c08f767e0fad7b/raw/5d752e5f0702da315298a6bb5a771586d6ff445c/wordle-answers-alphabetical.txt"
file = urllib.request.urlopen(url)

word_list = []

for raw_line in file:
    word = raw_line.decode("utf-8").strip()
    word_list.append(word)

x = len(word_list)
print (x)

# Print the 5 most common letters for each position
print(Counter(x[0] for x in word_list).most_common(5))
print(Counter(x[1] for x in word_list).most_common(5))
print(Counter(x[2] for x in word_list).most_common(5))
print(Counter(x[3] for x in word_list).most_common(5))
print(Counter(x[4] for x in word_list).most_common(5))

