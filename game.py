from ai import Ai
from human import Human

class Game:

    
    def __init__(self):
        self.player_one = None
        self.player_two = Human()
        


    def run_game(self):
        self.choose_players()
        self.display_rules()
        self.play_round() #while loop
       
    
        pass

    def display_rules(self):
        print(''' 
        The rules are as follows:
        ****************************
        
        Rock curshes Scissors
        Scissors covers Rock
        Rock crushed Lizard 
        Lizard poisons Spock
        Spock smashes Scissors
        Scissors decapitates Lizard
        Lizard eats Paper
        Paper disproves Spock
        Spock vaporizes Rock

        Let the game BEGIN!!!
        **********************
        ''')



    def choose_players(self):
        user_choice = input("would you like 1 or 2 human players")
        if user_choice == "1":
            self.player_one = Ai()
        elif user_choice == "2":
            self.player_one = Human()


    def play_round(self):
        print("Starting new round")
        self.player_one.attack()
        self.player_two.attack()
        if self.player_one.chosen_gesture == self.player_two.chosen_gesture:
            print("its a tie")
        elif self.player_one.chosen_gesture == "Rock" and self.player_two.chosen_gesture == "Scissors" or self.player_two.chosen_gesture == "Lizard":
            print("Player one wins")
            self.player_one.wins += 1
        elif self.player_one.chosen_gesture == "Paper" and self.player_two.chosen_gesture == "Rock" or self.player_two.chosen_gesture == "Spock":
            print("Player one wins")
            self.player_one.wins += 1
        elif self.player_one.chosen_gesture == "Scissors" and self.player_two.chosen_gesture == "Paper" or self.player_two.chosen_gesture == "Lizard":
            print("Player one wins")
            self.player_one.wins += 1
        elif self.player_one.chosen_gesture == "Lizard" and self.player_two.chosen_gesture == "Paper" or self.player_two.chosen_gesture == "Spock":
            print("Player one wins")
            self.player_one.wins += 1
        elif self.player_one.chosen_gesture == "Spock" and self.player_two.chosen_gesture == "Rock" or self.player_two.chosen_gesture == "Scissors":
            print("Player one wins")
            self.player_one.wins += 1
        else:
            self.player_two.wins += 1
            print("Player two wins")
            self.display_current_standing()
            
    def display_current_standing(self):
        print(f'{self.player_one.name} has {self.player_one.wins} wins')
        print(f'{self.player_two.name} has {self.player_two.wins} wins')
        
    
    def display_winner(self):
        pass



#Rock crushes Scissors 
# Scissors cuts Paper 
# Paper covers Rock 
# Rock crushes Lizard 
# Lizard poisons Spock 
# Spock smashes Scissors 
# Scissors decapitates Lizard
#Lizard eats Paper 
# Paper disproves Spock 
# Spock vaporizes Rock