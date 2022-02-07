from player import Player
import random

class Ai(Player):
    
    def __init__(self):
        self.name = 'George'
        super().__init__()

    def attack(self, human):
        self.chose_gesture = random.choice(self.list_of_gestures)
