import math

MIN_ASCII_CODE_NUMBER = 33
MAX_ASCII_CODE_NUMBER = 127


def main():

    character = input("Enter a character: ").strip()
    ascii_code = ord(character)
    print("The ASCII code for {} is {}".format(character, ascii_code))

    valid_number = False
    while not valid_number:
        prompt = "Enter a number between {} and {} (inclusive): ".format(MIN_ASCII_CODE_NUMBER, MAX_ASCII_CODE_NUMBER)
        ascii_code_number = int(input(prompt).strip())
        if MIN_ASCII_CODE_NUMBER <= ascii_code_number <= MAX_ASCII_CODE_NUMBER:
            valid_number = True
        else:
            print("Error, invalid number entered - outside of specified range")

    print("The character for {} is {}".format(ascii_code_number, chr(ascii_code_number)))

    for curr_code_number in range(MIN_ASCII_CODE_NUMBER, MAX_ASCII_CODE_NUMBER + 1):
        print("{:3} {:>3}".format(curr_code_number, chr(curr_code_number)))


    print("\n\n")

    number_of_columns = int(input("How many columns for ASCII display table? "))
    number_of_ascii_codes_to_print = MAX_ASCII_CODE_NUMBER - MIN_ASCII_CODE_NUMBER
    number_of_rows = int(math.ceil(float(number_of_ascii_codes_to_print) / number_of_columns))
    curr_code_number = MIN_ASCII_CODE_NUMBER
    for table_rows in range(number_of_rows):
        for column_index in range(number_of_columns):
            if not curr_code_number > MAX_ASCII_CODE_NUMBER:
                print("{:7}  {}".format(curr_code_number, chr(curr_code_number)), end='')
                curr_code_number += 1
        print("")


main()
