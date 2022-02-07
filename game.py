from ai import Ai
from human import Human

class Game:

    def __init__(self):
        self.player_one = None
        self.player_two = Human()

    def run_game(self):
        self.choose_player()
        pass

    def display_rules(self):
        pass

    def choose_players(self):
        user_choice = input("would you like 1 or 2 human players")
        if user_choice == "1":
            self.player_one = Ai()
        elif user_choice == "2":
            self.player_one = Human()


    def player_one_turn(self):
        pass

    def player_two_turn(self):
        pass


    def show_human_option(self):
        print(self.list_of_gestures)
        self.chose_gesture = input("Enter the number of the move you wish to make: ")
    
    def display_winner(self):
        pass



