import random

choices = ['rock', 'paper', 'scissors']
is_running = True
player_win =0
computer_win = 0

computer = random.choice(choices)

while is_running:
    
    player = None

    computer = random.choice(choices)

    while player not in choices:
        player = input("Make your choice : ").lower()

    if player == computer:
        print("PLAYER  ------ COMPUTER ")
        print(f"{player}------{computer}")
        print("No winner try again")

    elif player == 'rock' and computer == 'paper':
        print("PLAYER ------ COMPUTER ")
        print(f"{player} ------ {computer} ")
        print("Computer win!!")
        computer_win += 1

    elif player == 'rock' and computer == 'scissors':
        print("PLAYER  ------ COMPUTER ")
        print(f"{player} ------ {computer} ")
        print("Player win!!")
        player_win += 1

    elif player == 'paper' and computer == 'rock':
        print("PLAYER  ------ COMPUTER ")
        print(f"{player} ------ {computer} ")
        print("Player win!!")
        player_win += 1

    elif player == 'paper' and computer == 'scissors':
        print("PLAYER  ------ COMPUTER ")
        print(f"{player} ------ {computer} ")
        print("Computer win!!")
        computer_win += 1

    elif player == 'scissors' and computer == 'rock':
        print("PLAYER  ------ COMPUTER ")
        print(f"{player} ------ {computer} ")
        print("Computer win!!")
        computer_win += 1

    elif player == 'scissors' and computer == 'paper':
        print("PLAYER  ------ COMPUTER ")
        print(f"{player} ------ {computer} ")
        print("Player win!!")
        player_win += 1

    if not input("Play again? (Y/N) = ").lower() == "y":
        is_running = False

print()
print(f"Player win {player_win} times.")
print(f"Computer win {computer_win} times.")
print ()
print("Goodbye!")        

        




                        

