#ValueError
try:
    age = int(input("What is your age? "))
except ValueError:
    print("Please enter a valid age, such as '5'.")
else:
    print(f"Your age is {age}.")
finally: print("let's try again!")

#NameError
try:
    print(price)
except NameError: 
    print("Something went wrong!Python does not know the price! Please make sure it is defined!.")
else:
    print(f"The total price is {price}.")
finally:
    print("Happy Shopping!")

#TypeError
try:
    name = "Beatrice"
    age = 207
    print(name+age)
except TypeError:
    print("Oh no! Python can't calculate!/n"
          "Make sure you variables have the correct values!")
else:
    print("That's awesome!")
finally:
    print("Let's do this again!")

#SyntaxError
try:
    print("Hi nice to meet you")
except SyntaxError:
    print("Uh oh! Did you forget something in the syntax?")
else:
    print("My name is Sally.")
finally:
    print("What's your name?")

#Ironically, SyntaxErrors do not run the try-except code.