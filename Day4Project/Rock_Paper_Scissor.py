import random

Rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

Paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

Scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
choice = input("Choose from ROCK(1), PAPER(2) OR SCISSORS(3)")
possibilities = [Rock,Paper,Scissors]
myChoice = possibilities[int(choice)-1]
print(f' You chose {myChoice}')
computerChoice = possibilities[random.randint(0,2)]
print(f'Computer chose {computerChoice}')

if myChoice == possibilities[0] and computerChoice == possibilities[2]:
    print('You Won')
elif myChoice == possibilities[0] and computerChoice == possibilities[1]:
    print("You lost")
elif myChoice == possibilities[1] and computerChoice == possibilities[0]:
    print("You Won")
elif myChoice == possibilities[1] and computerChoice == possibilities[2]:
    print("You lost")
elif myChoice == possibilities[2] and computerChoice == possibilities[0]:
    print("You lost")
elif myChoice == possibilities[2] and computerChoice == possibilities[1]:
    print("You won")
else:
    print("It's a Draw")
