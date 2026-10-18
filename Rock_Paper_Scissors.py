import random
choices = ["rock", "paper", "scissors"]
wins = 0
losses = 0
draws = 0
while True:
    user = input("Choose rock, paper, scissors or quit: ").lower()
    if user == "quit":
        break
    if user not in choices:
        print("Invalid choice! Try again.")
        continue
    computer = random.choice(choices)
    print("Computer chose:", computer)
    if user == computer:
        print("It's a draw!")
        draws += 1
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("You win!")
        wins += 1
    else:
        print("Computer wins!")
        losses += 1
print("\nFINAL SCORE")
print("Wins:", wins)
print("Losses:", losses)
print("Draws:", draws)
