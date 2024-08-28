import Character from character
import Item from item
import playWordle from wordle

print("Welcome to the game!")
d1 = input("You come up to a field and see a star. Do you want to pick it up? (y/n)")
if d1 == "y":
    star = Item("Star", "A shiny star", 10)
    a1a print("You picked up the star, Yay! you see a man approaching you, do you want to talk to him? (y/n)")
    if d1a == "y": 
       character = Character("Man", 100, [], {"Hello, i am Mr Audieau"})
       character.talk_to_player("Hello, i am Mr Audieau")