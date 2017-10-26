def rotate_word(word, amount):
    new_word = ''
    for letter in word:
        if letter.isupper():
            new_word += chr(normalize(ord(letter) + amount, 65, 90))
        elif not letter.isalpha():
            new_word += letter
        else:
            new_word += chr(normalize(ord(letter) + amount, 97, 122))
return new_word
