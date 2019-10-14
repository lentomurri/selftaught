import re

# EXPERIMENTS WITH VARIABLE AND HANDLING ERRORS 

# num1 = input("Enter first number: ")
# num2 = input("Enter second number: ")

# def sumUp(x, y):
#     """
#     param x: int or float
#     param y: int or float
#     """
#     try:
#         x = float(x)
#         y = float(y)
#         print(x / y)
#     except (ZeroDivisionError, ValueError):
#         print("Please, enter only numbers and numbers different from 0.")

# print(sumUp(num1, num2))

# ----------------------
#PROGRAM TO SEARCH THROUGH VALUES AND FIND A CORRESPONDING KEY

list = ["dog", "cat", "bird"]
dictionary1 = {"BTS": ["Boy in Luv", "Idol"],
                "Placebo": ["Sleeping with ghosts"]}

# print("dog" in list)

def getKey(dict, listValues):
    # Gather all the list in the dictionary
    listOfItems = dict.items()
    # Iterate through the keys
    for item in listOfItems:
        # iterate through all the values
        for value in item[1]:
            # compare value to list of Valuew we are searching
            # if matching, gives us back the key
            if value in listValues:
                print(item[0])

getKey(dictionary1, ["Boy in Luv"])

# -- CHALLENGES --

# LIST OF FAVOURITE MUSICIANS

musicians = ["BTS", "Muse", "Placebo"]
cities = [ (42.837931, 13.931954), (37.830860, 12.481785), (51.556286, 0.000073)]
silvia = {"body": [{"height": 1.78, "eyes": "blue", "hair": "Half Blonde and Pink"}], "facts": [{"doggie": "Yoongi", "piculina": "Duru ti amu sei piculina duru"}]}

# Always use [BRACKETS] to search through a dictionary, together with the " for in"

# search through items in a dict
# search through keys for a specific one
for key in silvia["facts"]:
    # print the key matching to the one you want by using [brackets]
    print(key["doggie"])

#function to show users info about silvia

def findInfo():
    question = input("Which thing do you want to know? Body or facts? ").lower().strip()
    try:
        print(silvia[question])
    except KeyError:
        print("Please choose between Body and Facts")
        # after raising the error, we can start the function again
        findInfo()

# findInfo()

songs = {"BTS": ["Boy with Luv", "Spring Day", "Not Today", "Fire"], "Muse": ["Plug in baby", "Showbiz", "Muscle Museum"], "Placebo": ["Sleeping with ghosts", "36 Degrees", "English Summer Rain"]}

# print(songs)

camus = "Camus"

for letter in camus:
    print(letter)

# string1 = input("Insert a noun")
# string2 = input("Insert a person's name")

# print("Yesterday I wrote a {} and I sent it to {}" .format(string1, string2))
# print("yoongi is cute".capitalize())
exp = "Where now? Who Now? When Now?"

# print(re.split("( W+)", exp))

sentence = ["The", "white", "fox", "jumped",  "over", "the", "fence", "."]

sentence = " ".join(sentence[:7]) + sentence[7]

# print(sentence)

scream = "A screaming comes across the sky"
# print(scream.replace("s", "$"))

# print(scream.index("m"))

three = "three"

# print((three + " ") * 3)

bright = "It was bright cold, I made a painting"

print(bright[0:bright.index(",")])
