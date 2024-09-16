from character import Character 
from item import door, chocolate, key
from wordle import playWordle 

chocolate = chocolate()
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
    input("You go towards the light and find a house, do you go inside? y/n")
    if d2_a == "y":
        d3 = input("You went into the house, you find" + chocolate.name + "would you like to eat it? y/n")
    if d3 == "y":
        input("You eat the chocolate and feel better, However you see a strange man staring at you, and be begins to speak.") 
        chocolate.eat()
        character = Character("Man", 100, [], {"Hello, i am Mr Audieau"})
        character.talk_to_player("Hello, i am Mr Audieau, you are welcome to stay here! Congradulations you have won the game!")
    elif d2_a == "n":
            print("You stay outside and freeze to death game over")

def d2_b():
    input("You stay in the forst and are freezing cold as it turns night", life -1, "You see a shed, do you approach it? y/n")
    if d2_b == "y":
        d4 = input("You go into the shed, you find a" + key.name + "and a" + door.name + "would you like to use the key on the door? y/n")
        if d4 == "y":
            door.open = True
            print("You open the door and go inside, you find a a little boy laying on the ground, and he says to you")
            character = Character("Boy", 100, [], {"Hello, i am Ryan"})
            character.talk_to_player("Hello, i am Ryan, you are welcome to stay here! If you can beat this wordle you can win the game!")
            playWordle("ITEMS")
        if d4 == "n":
            print("you stay outside in the nigh all night, and die, game over")

