import os
from art import logo

clear = lambda: os.system('cls')


def winner(dict):

  highest = 0
  winnerName = 0

  for i in dict:

    if int(highest) < int(dict[i]):
      highest = dict[i]
      winnerName = i

  print(winnerName +" is the winner with "+ highest +"$")

print(logo)
dict = {}
checker = True

while (checker == True):
  name = input("What is your name ?: ")
  bid = input("What is your bid ?: $")

  dict[name] = bid

  clear()

  inp = input("Another bid ? y/n ")

  if (inp != 'y' and inp != 'Y'):
    checker = False

winner(dict)




