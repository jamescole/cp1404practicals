"""
CP1404/CP5632 Practical
Recursion
"""


def do_it(n):
    """Do... it."""
    if n <= 0:
        return 0
    return n % 2 + do_it(n - 1)


# TODO: 1. write down what you think the output of this will be,
# TODO: 2. use the debugger to step through and see what's actually happening
# print(do_it(5))


def do_something(n):
    """Print the squares of positive numbers from n down to 0."""
    if n < 0:
        return
    print(n ** 2)
    do_something(n - 1)

# TODO: 3. write down what you think the output of do_something(4) will be,
# TODO: 4. use the debugger to step through and see what's actually happening
# do_something(4)

# TODO: 5. fix do_something() so that it works according to the docstring


def do_something_ascending(n):
    """Print the squares of positive numbers from 0 to n."""
    if n < 0:
        return
    do_something_ascending(n - 1)
    print(n ** 2)


# do_something_ascending(5)


def calculate_blocks_in_2D_pyramid(rows):
    """
    Given a 2D pyramid with the given number of rows, where the nth row contains n blocks,
    return the number of blocks it contains.
    """

    number_of_blocks = 0
    for i in range(1, rows + 1):
        number_of_blocks += i

    return number_of_blocks


# print(calculate_blocks_in_2D_pyramid(6))


def calculate_blocks_in_2D_pyramid_recursive(rows):
    """
    Given a 2D pyramid with the given number of rows, where the nth row contains n blocks,
    return the number of blocks it contains.
    """

    if rows == 1:
        return 1
    return rows + calculate_blocks_in_2D_pyramid_recursive(rows - 1)


print(calculate_blocks_in_2D_pyramid_recursive(6))





