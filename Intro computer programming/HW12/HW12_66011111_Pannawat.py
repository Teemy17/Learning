#Q1
import re

worddict = {
    "be": "b",
    "because": "cuz",
    "see": "c",
    "the": "da",
    "okay": "ok",
    "are": "r",
    "you": "u",
    "without": "w/o",
    "why": "y",
    "see you": "cu",
    "ate": "8",
    "great": "gr8",
    "mate": "m8",
    "wait": "w8",
    "later": "l8r",
    "tomorrow": "2mro",
    "for": "4",
    "before": "b4",
    "once": "1ce",
    "and": "&",
    "Your": "ur",
    "You're": "ur",
    "As far as I know": "afaik",
    "As soon as possible": "ASAP",
    "At the moment": "atm",
    "Be right back": "brb",
    "By the way": "btw",
    "For your Information": "FYI",
    "In my humble opinion": "imho",
    "In my opinion": "imo",
    "Laughing out loud": "lol",
    "Oh my god": "omg",
    "Rolling on the floor laughing": "rofl",
    "Talk to you later": "ttyl",
}


def textese(s):
    text = s
    for key in worddict:
        text = text.replace(key, worddict[key])
    return text


def untextese(s):
    words = s.split()
    result = []

    for word in words:
        for key, value in worddict.items():
            if word == value:
                result.append(key)
                break
        else:
            result.append(word)

    return ' '.join(result)


print(textese("As far as I know, you are great!"))
print(untextese("cu l8r cuz ur gr8"))
#--------------------------------------------------------------------------------

#Q2
def composite(dict1, dict2):
    dict3 = {}
    for keydict1 in dict1:
        for keydict2 in dict2:
            if dict1[keydict1] == keydict2:
                dict3[keydict1] = dict2[keydict2]
    return dict3

dict1 = {'a' : 'p', 'b' : 'r', 'c' : 'q', 'd' : 'p', 'e' : 's'}
dict2 = {'p' : 1, 'q' : 2, 'r' : 3}

print(composite(dict1, dict2))
#--------------------------------------------------------------------------------

#Q3
def cartesian_product(*sets):
    if len(sets) == 1:
        return sets[0]
    else:
        return set([(x, y) for x in sets[0] for y in cartesian_product(*sets[1:])])
    
s1 = set([1, 2, 3])
s2 = set(['p', 'q'])
s3 = set(['a', 'b', 'c'])

print(cartesian_product(s1, s2))
print(cartesian_product(s1, s2, s3))
print(cartesian_product(s1))

