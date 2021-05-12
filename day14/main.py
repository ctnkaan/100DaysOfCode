from art import logo,vs
from game_data import data
from replit import clear

score = 0


for i in range(48):
  print(logo)

  print("\nScore: ",score)
  print("1 - ",data[i]["name"])
  print(data[i]["description"])
  
  print(vs)

  print("2 - ",data[i+1]["name"])
  print(data[i]["description"])

  userInp= int(input("> "))

  if userInp == 1:
    if data[i]["follower_count"] > data[i+1]["follower_count"]:
      score+=1
    else:
      print("You lose. With a score of ",score)
      exit(0)
  elif userInp == 2:
    if data[i]["follower_count"] < data[i+1]["follower_count"]:
      score+=1
    else:
      print("You lose. With a score of ",score)
      exit(0)
  else:
    exit("Illegal input")

  clear()

print("You got all right. Well done !")

