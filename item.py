class chocolate:
    def __init__(self):
        self.name = "chocolate"
        self.description = "chocolate bar"
        self.healing = 1


    def eat(self, player):
        player.health += self.healing
        self.healing = 0


class key:
    def __init__(self):
        self.name = "key"
        self.description = "A key to open a door"
        self.unlock = True
    def usekey(self, door):
        door.open = True
class door:
    def __init__(self):
        self.name = "door"
        self.description = "A door that requires a key"
        self.open = False