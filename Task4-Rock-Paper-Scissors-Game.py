import random

options = ["rock", "paper", "scissors"]
user_score = 0
computer_score = 0

def get_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"

while True:
    print("\nRock, Paper, Scissors")
    user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
    if user_choice not in options:
        print("Invalid choice.")
        continue

    computer_choice = random.choice(options)
    print(f"Computer chose: {computer_choice}")

    winner = get_winner(user_choice, computer_choice)
    if winner == "tie":
        print("It's a tie!")
    elif winner == "user":
        print("You win!")
        user_score += 1
    else:
        print("Computer wins!")
        computer_score += 1

    print(f"Score - You: {user_score}, Computer: {computer_score}")

    play_again = input("Play again? (y/n): ").lower()
    if play_again != 'y':
        break
