def main():
    string = input("Text: ")
    word_counts = get_word_counts(string)
    print_word_counts(word_counts)


def get_word_counts(string):
    words = string.split(' ')
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts


def print_word_counts(word_counts):
    word_column_width = get_longest_string_length(word_counts.keys())
    for word in sorted(word_counts.keys()):
        print("{:{}} : {}".format(word, word_column_width, word_counts[word]))


def get_longest_string_length(string_list):
    longest_string_length = 0
    for string in string_list:
        if len(string) > longest_string_length:
            longest_string_length = len(string)
    return longest_string_length


main()
