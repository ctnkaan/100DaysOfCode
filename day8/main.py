from art import logo

def crpyt(txt,shift,direction):

  shift %= 26
  new_txt = ""

  for letter in txt:
    pos = alphabet.index(letter)
    if direction == "encode":
      pos+=shift
    elif direction == "decode":
      pos -= shift
    else:
      print("Illegal User Input")
      exit(1)
    letter = alphabet[pos]
    new_txt += letter
  print("The cypher text is "+new_txt+"\n")

running = True

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

while running == True :
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  crpyt(text,shift,direction)

  inp = input("Press 1 for again\nPress any other button to exit\n")

  if inp != '1':
    running = False
  
