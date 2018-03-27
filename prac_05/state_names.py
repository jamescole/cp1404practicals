"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""


def print_state_abbreviations_and_names():
    for state_abbreviation in STATE_NAMES:
        print("{:4} is {}".format(state_abbreviation, STATE_NAMES[state_abbreviation]))


STATE_NAMES = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
               "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
# print(STATE_NAMES)

print_state_abbreviations_and_names()
print()

state = input("Enter short state: ").upper()
while state != "":
    if state in STATE_NAMES:
        print(state, "is", STATE_NAMES[state])
    else:
        print("Invalid short state")
    state = input("Enter short state: ").upper()
