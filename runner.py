import Character from character
import Item from item
import playWordle from wordle

print("Welcome to the game!")
d1 = input("You are walking in a forest, do you A. go deeper, B. leave, or C. go off the path?")
if d1 == "A":
    d1_a = input("You decide to keep walking in the forest, as you go deeper you see a light, Do you go towards the light y/n?")
    if d1_a == "y":
        d2_a()
    elif d1_a =="n":
        d2_b

elif d1 == "B":
    print("You try to leave, but are attacked by wolves and have lost a life, chose a different answer.", life-1)
elif d1 == "C":
    print("You trip and scrape yourself on some rocks, but see a light. Do you go towards the light y/n")
    if d1_a == "y":
        d2_a()
    elif d1_a =="n":
        d2_b

def d2_a():
    print("You went into the house")

def d2_b():
    print("You stay in the forst and are freezing cold as it turns night", life -1)


else:
    print("You entered wrong, try again.")
    star = Item("Star", "A shiny star", 10)
    a1a print("You picked up the star, Yay! you see a man approaching you, do you want to talk to him? (y/n)")
    if d1a == "y": 
       character = Character("Man", 100, [], {"Hello, i am Mr Audieau"})
       character.talk_to_player("Hello, i am Mr Audieau")