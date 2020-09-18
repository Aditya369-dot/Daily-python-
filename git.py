print ("hello world")


# creating my own dictionary 

import json 

data = json.load(open("data.json"))

def translate(w):
    if w in data:
        return data[w]
    else:
        return "the word doesnt exist. please double check it."

word = input("enter word: ")

print(translate(word))