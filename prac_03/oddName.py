"""
Asks the user for their name, checks it isn't blank, then prints every second letter in the name.

James Cole
"""

name = input("Enter your name: ")
while name == "":
    print("Error, empty name string")
    name = input("Enter your name: ")
print(name[1::2])
