"""
Create a Rock Paper Scissors game where the player inputs their choice
and plays  against a computer that randomly selects its move, 
with the game showing who won each round.
Add a score counter that tracks player and computer wins, 
and allow the game to continue until the player types “quit”.
""" 
import random
def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"
def main():
    player_score = 0
    computer_score = 0
    while True:
        player_input = input("Enter rock (r), paper (p), scissors (s) or quit to exit: ").lower()
        
        # Map shortcuts to full names
        choice_map = {'r': 'rock', 'p': 'paper', 's': 'scissors'}
        player_choice = choice_map.get(player_input, player_input)
        if player_choice == 'quit':
            print("Thanks for playing!")
            break
        if player_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please try again.")
            continue
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        result = determine_winner(player_choice, computer_choice)
        print(result)
        if result == "You win!":
            player_score += 1
        elif result == "Computer wins!":
            computer_score += 1
        print(f"Score - You: {player_score}, Computer: {computer_score}\n")

if __name__ == "__main__":
    main()
