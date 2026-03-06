import random as r

print("WELCOME!!")
print("Type Rock, Paper, or Scissors")

while True:

    user = input("Enter your choice: ").lower()

    choices = ["rock", "paper", "scissors"]

    if user not in choices:
        print("Invalid choice. Try again.")
        continue

    cp = r.choice(choices)

    print("Computer chose:", cp)

    if user == cp:
        print("It's a tie!")
    elif (user == "rock" and cp == "scissors") or \
         (user == "paper" and cp == "rock") or \
         (user == "scissors" and cp == "paper"):
        print("User wins!")
    else:
        print("Computer wins!")

    again = input("Play again (Y/N): ")

    if again.upper() == "N":
        print("Thanks for playing!")
        break