from player import Player
class Human(Player):

    def __init__ (self):
        super().__init__()
        self.set_name()

    def attack(self):
        valid = False
        counter = 0
        for gesture in self.list_of_gestures:
            print(f'Press {counter} to select {gesture}')
            counter += 1
        while valid == False:
            user_choice = int(input("Enter the number of the move you wish to make: "))
            if user_choice <= 4 and user_choice >= 0:
                valid = True
            else:
                print("please enter a valid reponse")
        self.chosen_gesture = self.list_of_gestures[user_choice]
        print(f'{self.chosen_gesture} picked by human')

    def set_name(self):
        self.name = input("What is your name?")


        