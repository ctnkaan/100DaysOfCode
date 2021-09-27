from art import logo

def addition(fnum,snum):
  return fnum + snum

def sub(fnum,snum):
  return fnum - snum

def divide(fnum,snum):
  return fnum / snum

def multiply(fnum, snum):
  return fnum * snum


print(logo)

fnum = int(input("Enter the first number: "))
op = input("+ - / * pick an operation: ")
snum = int(input("Enter the second number: "))

if (op == '+'):
  print(addition(fnum,snum))
elif (op == '-'):
  print(sub(fnum,snum))
elif (op == '/'):
  print(divide(fnum,snum))
elif (op == '*'):
  print(multiply(fnum,snum))
else:
  print("Error")