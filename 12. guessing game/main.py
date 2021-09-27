import random

guess = random.randint(1,100)
lives = 10

print("Welcome to the Number Guessing Game!")
print("\nGuess my number between 1-100")

diff = int(input("Press 1 for easy, press 2 for hard "))

hard = False

if diff == 2:
  hard = True

if hard == True:
  lives = 5

print("You have ", lives, " lives")
userInp = int(input("Make a guess: "))

while userInp != guess and lives > 0:
  if userInp > guess:
    print("Too high\n\n")
  else:
    print("Too low\n\n")
  lives-=1
  print("You have ",lives," lives")
  userInp = int(input("Make a guess: "))

if lives <= 0:
  print("You loose. The number was ",guess)
else:
  print("You win !")