import os
import sys
import re

def removeSMGL(text):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

def tokenizeText(text):
    tokens = []
    words = text.split()
    # Split() splits the string by spaces
    for word in words:
        # Tokenize '.'
        if "." in word and len(word) > 1:
            if word[len(word)-1] == ".":
                word = word.replace(".", " .")
            if not word.replace(".", "").isdigit():
                word = word.replace(".", " . ")
        # Tokenize '''
        if "'" in word and len(word) > 1:
            if word.index("'") == len(word)-1:
                word = word.replace("'", " '")
            elif word[word.index("'")+1] == 's':
                if word[0][0].isupper():
                    word = word.split("'")
                    word = word[0]
                    tokens.append("'s")
                else:
                    word = word.split("'")
                    word = word[0]
                    tokens.append('is')  
            elif word[word.index("'")+1] == 'm':      
                word = word[0]
                tokens.append("am")
            else:
                word = word.replace("'", " ' ") 
        # Tokenize / except for dates
        if "/" in word:
            if word[len(word)-1] == "/" or word[0] == "/":
                word = word.replace("/", "/ ")
            if not word.replace('/', '').isdigit():
                word = word.replace("/", " / ")
        # Tokenize ','
        if "," in word and len(word) > 1:
            if word[len(word)-1] == ",":
                word = word.replace(",", " ,")
            if not word.replace(",", "").isdigit():
                word = word.replace(",", " , ")
        # Other punc
        if "(" in word:
            word = word.replace("(", " ( ")
        if ")" in word:
            word = word.replace(")", " ) ")
        if "?" in word:
            word = word.replace("?", " ? ")
        tokens.extend(word.split())
    return tokens


