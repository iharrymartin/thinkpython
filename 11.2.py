def histogram(word):
    dictionary = dict()
    for character in word:
        dictionary[character] = 1 + dictionary.get(character, 0)
    return dictionary
print histogram('asdfghjklpoiuyttr')
