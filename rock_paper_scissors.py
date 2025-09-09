import random

users_wins=0
computer_wins=0

options=["rock","paper","scissors"]
options[0]

while True:
    users_input=input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if users_input=="q":
        break

    if users_input not in options:
        continue

    random_number=random.randint(0,2)
    # rock:0, paper:1, scissors:2
         

print("Goodbye!")
