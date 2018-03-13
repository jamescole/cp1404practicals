"""
CP1404/CP5632 - Practical
Broken program to determine score status

score must be between 0 and 100 inclusive; 90 or more is excellent; 50 or more is a pass; below 50 is bad
"""


def main():
    score = float(input("Enter score: "))
    if score < 0 or score > 100:
        print("Invalid score")
    else:
        result = get_result_for_score(score)
        print(result)


def get_result_for_score(score):
    """
    Assumes score is >= 0 and <= 100
    """
    if score >= 90:
        result = "Excellent"
    elif score >= 50:
        result = "Pass"
    else:
        result = "Bad"
    return result


main()
