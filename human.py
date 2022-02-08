from player import Player
class Human(Player):

    def __init__ (self):
        super().__init__()
        self.set_name()

    def attack(self):
        valid = ("0","1","2","3","4") 
        counter = 0
        for gesture in self.list_of_gestures:
            print(f'Press {counter} to select {gesture}')
            counter += 1
        user_choice = input("Enter the number of the move you wish to make: ")
        while user_choice not in valid:
            user_choice = input("invalid input, try again")
        self.chosen_gesture = self.list_of_gestures[int(user_choice)]
        print(f'{self.chosen_gesture} picked by human')

    def set_name(self):
        self.name = input("What is your name?")


        