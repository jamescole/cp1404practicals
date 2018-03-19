def main():
    numbers = []
    print("Enter negative value to stop entering inputs.")
    number = int(input("Number {}: ".format(len(numbers) + 1)))
    while number >= 0:
        numbers.append(number)
        number = int(input("Number {}: ".format(len(numbers) + 1)))

    print("The first number is {}".format(numbers[0]))
    print("The last number is {}".format(numbers[-1]))
    print("The smallest number is {}".format(min(numbers)))
    print("The largest number is {}".format(max(numbers)))
    print("The average of the numbers is {}".format(sum(numbers) / len(numbers)))


main()
