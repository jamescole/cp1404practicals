finished = False
result = 0
while not finished:
    try:
        result = int(raw_input("Enter number: "))
        finished = True
    except ValueError:
        print("Please enter a valid integer")
print("Valid result is: " + str(result))


