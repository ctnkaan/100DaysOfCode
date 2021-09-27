rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

player = 0

player = int(input("Press 0 for Rock, 1 for Paper, 2 for Scissors\n"))

if (player != 0 and player != 1 and player != 2):
  print("You must enter 0, 1 or 2. Exitting\n")
  exit(0)

print("You Choose\n")
if player == 0:
  print(rock)
elif player == 1:
  print(paper)
else:
  print(scissors)


cpu = int(random.random() * 3)

print("Computer Choose\n")
if cpu == 0:
  print(rock)
elif cpu == 1:
  print(paper)
else:
  print(scissors)

if player == cpu:
  print("Draw")
elif player == 0 and cpu == 1:
  print("CPU wins")
elif player == 1 and cpu == 2:
  print("CPU wins")
elif player == 2 and cpu == 1:
  print("CPU wins")
else:
  print("Player wins")  