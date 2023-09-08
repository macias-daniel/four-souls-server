from classes.Character import Character


class Player:
    def __init__(self, ID) -> None:
        self.ID = ID

    #    self.character = character

    def getName(self):
        return self.name

    def getCharacter(self):
        return self.character

    def setName(self, name):
        self.name = name

    def setCharacter(self, character):
        self.character = character
