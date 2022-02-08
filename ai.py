from player import Player
import random

class Ai(Player):
    
    def __init__(self):
        super().__init__()
        self.set_name()


    def attack(self):
        self.chosen_gesture = random.choice(self.list_of_gestures)
        print(f'{self.name} has picked {self.chosen_gesture}')

    def set_name(self):
        self.name = "George"