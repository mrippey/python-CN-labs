import random 
import sys 

player_hand = input('Player1, enter the numbers 0 - 2 to pick your hand: ')

def get_hand(hand=player_hand):
    rps_hand = {"0": "scissors", "1": "rock", "2": "paper"}
    opponent_computer = random.choice(['scissors', 'rock', 'paper'])
    player1_hand = rps_hand.get(hand)
    
    print(f'Player1: {player1_hand} Computer: {opponent_computer}')
    

    def determine_winner():
        if player1_hand == opponent_computer:
            print("It's a draw! Try again")
            sys.exit()

        elif (
            player1_hand == 'rock'
            and opponent_computer == 'paper'
            or player1_hand == 'rock'
            and opponent_computer == 'scissors'
            or player1_hand == 'scissors'
            and opponent_computer == 'paper'
            or player1_hand == 'paper'
            and opponent_computer == 'rock'
        ):
            print('Player1 Wins')

        elif (
            opponent_computer == 'rock' 
            and player1_hand == 'paper'
            or opponent_computer == 'scissors' 
            and player1_hand == 'rock'
            or opponent_computer == 'scissors'
            and player1_hand == 'paper'
            
        ):
            print('Computer Wins')
        else:
            print('An error occurred')

    determine_winner()

get_hand()

