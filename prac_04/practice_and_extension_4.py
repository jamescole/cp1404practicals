def main():
    list1 = [1, 2, 3, 1, 1, 1, 1]
    list2 = [2, 7, -14, 4, 11]
    memberwise_addition_list = memberwise_addition(list1, list2)
    print(memberwise_addition_list)


def memberwise_addition(list1, list2):
    """
    Returns the list that contains the sum of elements that are in the same index in the two lists.
    """
    longest_list, shortest_list = [], []
    if len(list1) > len(list2):
        longest_list = list1
        shortest_list = list2
    else:
        longest_list = list2
        shortest_list = list1
    memberwise_addition_list = [shortest_list_number + longest_list[i] for i, shortest_list_number in
                                enumerate(shortest_list)]
    if len(list1) != len(list2):
        memberwise_addition_list += longest_list[len(shortest_list):]
    return memberwise_addition_list


main()
