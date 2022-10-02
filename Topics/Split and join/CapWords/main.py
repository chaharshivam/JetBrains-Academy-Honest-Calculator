phrase = input().split("_")
new_phrase = list()
for word in phrase:
    new_phrase.append(word.title())
print("".join(new_phrase))
