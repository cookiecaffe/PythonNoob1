print("Welcome to coffe shop")

name = input("what is your name ?\n")

if name == "Ben":
    print("You are not allowed here, please get out !!")
    exit()



else:
    print("Hello " + name + " ,thanks for coming here today\n\n")



#coffe menu
menu = "Black coffe , Latte , Espresso  "

print(name + " what would you like from our menu ? here is what we have.\n" + menu)

order = input()

price = 12

quantity = input("How many coffees would you like ?\n")

total = price * int(quantity)

print("Thank you, your total is: €" + str(total))

print("Allright " + name + " ,i will get your " + quantity + " " + order + " in a moment ")

