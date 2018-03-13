valid_number = False
while not valid_number:
    prompt = "Enter a number between {} and {} (inclusive): ".format(MIN_ASCII_CODE_NUMBER, MAX_ASCII_CODE_NUMBER)
    ascii_code_number = int(raw_input(prompt).strip())
    if MIN_ASCII_CODE_NUMBER <= ascii_code_number <= MAX_ASCII_CODE_NUMBER:
        valid_number = True
    else:
        print("Error, invalid number entered - outside of specified range")





ascii_code_number = int(raw_input("Enter a number between {} and {} (inclusive):".format(MIN_ASCII_CODE_NUMBER, MAX_ASCII_CODE_NUMBER)).strip())

while MIN_ASCII_CODE_NUMBER > ascii_code_number > MAX_ASCII_CODE_NUMBER:

        print("Error, invalid number entered - outside of specified range")
