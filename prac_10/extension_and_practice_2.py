

def main():
    assert is_palindrome("abba")
    assert is_palindrome("radar")
    assert is_palindrome("a")
    assert is_palindrome("hannah")
    assert is_palindrome("Hannah")
    assert not is_palindrome("Dog")
    assert not is_palindrome("radaar")


def is_palindrome(string):
    """Check whether or not a string is a palindrome."""

    string = string.lower()  # not bothering with efficiency
    if len(string) <= 1:
        return True
    else:
        if string[0] != string[-1]:
            return False
        else:
            return is_palindrome(string[1:-1])


main()
