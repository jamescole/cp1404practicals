from __future__ import print_function

NAMES_FILE_NAME = "names.txt"

# user_name = raw_input("Enter your name: ")
# name_file = open(NAMES_FILE_NAME, "w")
# print(user_name, file=name_file)
# name_file.close()


# name_file = open(NAMES_FILE_NAME, "r")
# name = name_file.readline().strip()
# print("Your name is " + name)
# name_file.close()


NUMBERS_FILE_NAME = "numbers.txt"
numbers_file = open(NUMBERS_FILE_NAME, "r")
total = 0
for line in numbers_file:
    total += int(line)
print("total is " + str(total))
numbers_file.close()
