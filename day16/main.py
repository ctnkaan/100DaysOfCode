from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#Object declerations
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()


is_on = True

coffee_maker.report()
money_machine.report()

while is_on:
  options = menu.get_items()
  user_input = input(f"What would you like ? {options} ")

  if user_input == "off":
    is_on = False
  
  elif user_input != 'latte' and user_input != 'espresso' and user_input != 'cappuccino':
    print("Error")

  elif user_input == "report":
    coffee_maker.report()
    money_machine.report()

  else:
    drink = menu.find_drink(user_input)
    if coffee_maker.is_resource_sufficient(drink):
      if money_machine.make_payment(drink.cost):
        print("Sucsessfull Payment!")
        coffee_maker.make_coffee(drink)
      else:
        print("Unsucsessfull Payment")
    else:
      print("Not enough resources")
  print("\n\n")