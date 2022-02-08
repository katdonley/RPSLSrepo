from player import Player
class Human(Player):

    def __init__ (self):
        super().__init__()
        self.set_name()

    def attack(self):
        counter = 0
        for gesture in self.list_of_gestures:
            print(f'Press {counter} to select {gesture}')
            counter += 1
        user_choice = int(input("Enter the number of the move you wish to make: "))
        self.chosen_gesture = self.list_of_gestures[user_choice]
        print(f'{self.chosen_gesture} picked by human')

    def set_name(self):
        self.name = input("What is your name?")