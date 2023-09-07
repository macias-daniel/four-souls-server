from classes.Character import Character


class Player:
    def __init__(self, name, character) -> None:
        self.name = name
        self.character = character

    def getName(self):
        return self.name

    def getCharacter(self):
        return self.character
