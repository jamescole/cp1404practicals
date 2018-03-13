"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    valid_denominator = False
    while not valid_denominator:
        denominator = int(input("Enter the denominator: "))
        if denominator == 0:
            print("invalid denominator - must be non-zero")
        else:
            valid_denominator = True
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
