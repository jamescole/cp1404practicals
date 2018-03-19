"""
CP1404/CP5632 Practical
Debugging exercise: almost-working version of a CSV scores file program.
The scores.csv file stores scores for each subject for 10 people.
This code reads the lines into lists, saves the first line as a list of subject codes and
converts the rest of the lines from a list of strings into a list of numbers,
which it then prints with the maximum value for that subject.
Nice. Except, it’s broken! It reads the lists per user not per subject so the results are incorrect.
Use the debugger to follow what it's doing... then fix it.
"""


def main():
    """Read and display student scores from scores file."""
    scores_file = open("scores.csv")
    scores_data = scores_file.readlines()
    print(scores_data)
    subjects = scores_data[0].strip().split(",")
    score_values = []
    for score_line in scores_data[1:]:
        score_strings = score_line.strip().split(",")
        score_numbers = [int(value) for value in score_strings]
        score_values.append(score_numbers)
    scores_file.close()
    for subject_index in range(len(subjects)):
        print(subjects[subject_index], "Scores:")
        print("-------------")
        scores_for_subject = [score_values[student_index][subject_index] for student_index in range(len(score_values))]
        for score in scores_for_subject:
            print("{:3}".format(score))
        print("-------------")
        print("Min: {:<3}".format(min(scores_for_subject)))
        print("Max: {:<3}".format(max(scores_for_subject)))
        print("Avg: {:<3}".format(sum(scores_for_subject) / len(scores_for_subject)))
        print("\n")


main()
