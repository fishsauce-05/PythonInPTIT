words = list(input().split(' '))
words.sort(key=len, reverse=True)
print(words[0], len(words[0]))