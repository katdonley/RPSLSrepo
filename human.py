from player import Player
class Human(Player):

    def __init__ (self):
        self.name = 'Player Two'
        super().__init__()

    def attack(self):

        