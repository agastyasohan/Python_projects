
import random

def get_choices():
	options = ["rock", "paper", "scissors"]

	while True:
		player_choice = input("Enter a choice (rock, paper, scissors):").lower()
		if player_choice in options:
			computer_choice = random.choice(options)
			choices = {"player": player_choice, "computer": computer_choice}
			return choices	
		else:
			print("Invalid Choice!. Please Try again:")
	

def check_win(player,computer):
	print(f"you chose {player}, computer chose {computer}\n")
	
	if player == computer:
		return "'It's a tie!'"
	elif player == "rock":
		if computer == "paper":
			return "'Paper covers rock! You lose.'"
		else:
			return "'Rock smashes scissors! You win!'"
	elif player == "paper":
		if computer == "rock":
			return "'Paper covers rock! You Win!'"
		else:
			return "'scissors cuts Paper! You lose.'"
	

# main function
while True:
	choices_dict = get_choices() # it is a dictionary that stores the choices made by player and computer.
	result = check_win(choices_dict["player"], choices_dict["computer"])
	print(result)
	print()

	play_again = input("Play again? (y/n)")
	if play_again.lower() != "y":
		break
