print ("Hello world")

import random

RANKS = [1, 2, 3, 4, 5, 6]

class Game: 
    def __init__(self):
        self.player = Player("Brandon")
        self.dealer = Dealer("Computer")
        self.dice = Dice()
        self.total_computer_score = 0
        self.total_player_score = 0

    
    def player_round(self):
        print("Your current total score is: " f'{self.total_player_score}')
        choice = 'r'
        while choice == 'r':
            choice = input("Do you want to (r)oll or (h)old? ")
            if choice == 'h':
                break
            self.dice.roll_dice(self.player)
            if self.player.round_score == 0:
                break  
        self.total_player_score += self.player.round_score
        if self.total_player_score >= 100:
            self.end_game()
        else:
            print("Your total score is: " f'{self.total_player_score}' ". It is now the Computer's turn.")
            print("")
            self.player.round_score = 0
            self.computer_round()
                

    def computer_round(self):
        self.dealer.round_score = 0
        while self.dealer.round_score <= 20:
            self.dice.roll_dice(self.dealer)
            if self.dealer.round_score == 0:
                print ("The Computer's total score is: " f'{self.total_computer_score}' ". It is now the Player's turn.")
                print ("")
                self.dealer.round_score = 0
                self.player_round()
            if self.dealer.round_score >= 20:
                self.total_computer_score += self.dealer.round_score
                if self.total_computer_score >= 100:
                    self.end_game()
                else:
                    print ("The Computer's total score is: " f'{self.total_computer_score}' ". It is now the Player's turn.")
                    print ("")
                    self.dealer.round_score = 0
                    self.player_round()
            
            

    def choose_starting_player(self):
        rng = random.choice(RANKS)
        if rng < 4: 
            game.player_round()
        else: 
            game.computer_round()

    def end_game(self):
        if self.total_computer_score > 100:
            print("Game over!  Computer has reached 100.")
            self.reset()
        if self.total_player_score > 100:
            print("You win!")
            self.reset()

    def reset(self):
        reset_game = input("Enter 'reset' to restart the game and roll your first dice.  Enter anything else to exit. ")
        if reset_game == "reset":
            self.total_player_score = 0
            self.total_computer_score = 0
            print("")
            game = Game()
            game.choose_starting_player()
        else: 
            exit()

                      
class Player: 
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.round_score = 0 

    def __str__(self):
        return f'{self.name}'


class Dealer: 
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.round_score = 0

    def __str__(self):
        return f'{self.name}'


class Dice: 
    def __init__(self):
        self.faces = RANKS

    def roll_dice(self, participant):
        roll = random.choice(self.faces)
        int_roll = int(str(roll))
        if int_roll != 1:
            participant.round_score += int_roll
            print (f'{participant}' " rolled a " f'{int_roll}')
            print (f'{participant}' "'s current round score is: " + str(participant.round_score))
        else: 
            participant.round_score = 0
            print (f'{participant}' " rolled a " f'{int_roll}')
            print (f'{participant}' "'s turn is now over.  "  f'{participant}'"'s round score is: " + str(participant.round_score))
        

    def __str__(self):
        return f'(self.rank)'


class DiceFace: 
    def __init__(self, rank):
        self.rank=rank

    def __str__(self):
        return f'{self.rank}'


game = Game()
game.choose_starting_player()
# game.round()


#=========Notes and other nonsense=============================

# def player_round(self):
#         print("Your current total score is: " f'{self.total_player_score}')
#         choice = input("Do you want to (r)oll or (h)old?")
#         while choice == 'r':
#             self.dice.roll_dice(self.player)
#             choice = input("Do you want to (r)oll or (h)old?")
#             if choice == 'h':
#                 self.total_player_score += self.player.round_score
#                 print("Your total score is: " f'{self.total_player_score}')
#                 self.computer_round()


# This kinda works.  
# print ("Hello world")

# import random

# RANKS = [1, 2, 3, 4, 5, 6]

# class Game: 
#     def __init__(self):
#         self.player = Player("Brandon")
#         self.dealer = Dealer("Computer")
#         self.dice = Dice()
#         self.total_computer_score = 0
#         self.total_player_score = 0

    
#     def player_round(self):
#         self.player.round_score == 0
#         print("Your current total score is: " f'{self.total_player_score}')
#         choice = 'r'
#         while choice == 'r':
#             choice = input("Do you want to (r)oll or (h)old?")
#             if choice == 'h':
#                 break
#             self.dice.roll_dice(self.player)
#             if self.player.round_score == 0:
#                 break  
#         self.total_player_score += self.player.round_score
#         print("Your total score is: " f'{self.total_player_score}' ". It is now the Computer's turn.")
#         print("")
#         game.computer_round()
                

#     def computer_round(self):
#         self.dealer.round_score == 0
#         while self.dealer.round_score <= 20:
#             self.dice.roll_dice(self.dealer)
#             if self.dealer.round_score == 0:
#                 print ("The Computer's total score is: " f'{self.total_computer_score}' ". It is now the Player's turn.")
#                 print ("")
#                 game.player_round()
#             if self.dealer.round_score >= 20:
#                 self.total_computer_score += self.dealer.round_score
#                 print ("The Computer's total score is: " f'{self.total_computer_score}' ". It is now the Player's turn.")
#                 print ("")
#                 game.player_round()
            

#     def choose_starting_player(self):
#         rng = random.choice(RANKS)
#         if rng < 4: 
#             game.player_round()
#         else: 
#             game.computer_round()

#     def end_game(self):
#         if self.total_computer_score > 100:
#             print("Game over!  Computer has reached 100.")
#             self.reset()
#         if self.total_player_score > 100:
#             print("You win!")
#             self.reset()

#     def reset(self):
#         reset_game = input("Enter 'reset' to restart the game and roll your first dice.  Enter anything else to exit.")
#         if reset_game == "reset":
#             self.total_player_score = 0
#             self.total_computer_score = 0
#             print("")
#             game = Game()
#             game.choose_starting_player()

                      
# class Player: 
#     def __init__(self, name):
#         self.name = name
#         self.score = 0
#         self.round_score = 0 

#     def __str__(self):
#         return f'{self.name}'


# class Dealer: 
#     def __init__(self, name):
#         self.name = name
#         self.score = 0
#         self.round_score = 0

#     def __str__(self):
#         return f'{self.name}'


# class Dice: 
#     def __init__(self):
#         self.faces = RANKS

#     def roll_dice(self, participant):
#         roll = random.choice(self.faces)
#         int_roll = int(str(roll))
#         if int_roll != 1:
#             participant.round_score += int_roll
#             print (f'{participant}' " rolled a " f'{int_roll}')
#             print (f'{participant}' "'s current round score is: " + str(participant.round_score))
#         else: 
#             participant.round_score = 0
#             print (f'{participant}' " rolled a " f'{int_roll}')
#             print (f'{participant}' "'s turn is now over.  "  f'{participant}'"'s round score is: " + str(participant.round_score))
    
#     def __str__(self):
#         return f'(self.rank)'


# class DiceFace: 
#     def __init__(self, rank):
#         self.rank=rank

#     def __str__(self):
#         return f'{self.rank}'


# game = Game()
# game.choose_starting_player()
# game.round()