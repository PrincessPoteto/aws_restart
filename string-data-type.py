myString = "This is a string."
print(myString)
print(type(myString))
print(myString + " is of the data type " + str(type(myString)))
# Ejercicio 2 Lab 3
firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)

# Ejercicio 3 Lab 3
name = input("What is your name? ")
print(name)
# Ejercicio 4 Lab3
color = input("What is your favorite color?  ")
animal = input("What is your favorite animal?  ")
print("{}, you like a {} {}!".format(name,color,animal))
print(f"{name}, you like a {color} {animal}!")