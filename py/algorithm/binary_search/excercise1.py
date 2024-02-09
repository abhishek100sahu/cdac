################### PROBLEM 2 #######################
# Problem: Find index of all the occurances of a number from sorted list
# Solution here tries to find an index of a number using binary search. Now since the list is sorted,
# it can do left and right scan from the initial index to find all occurances of a given element
# This method is not most efficient and I want you to figure out even a better way of doing it. In
# any case below method is still effective


def binary_search(number_list, number_to_search):
    left_index = 0
    right_index = len(number_list) - 1
    mid_index = 0

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2

        mid_number = number_list[mid_index]

        if number_to_search == mid_number:
            return mid_index

        if number_to_search < mid_number:
            right_index = mid_index - 1
        else:
            left_index = mid_index + 1

    return -1


def find_all_occurrences(number_list, number_to_search):
    index = binary_search(number_list=number_list, number_to_search=number_to_search)

    indices = [index]

    # find indices on left side

    i = index - 1

    while i >= 0:
        if number_to_search == number_list[i]:
            indices.append(i)
        else:
            break
        i -= 1

    # find indices on right side

    i = index + 1

    while i < len(number_list):
        if number_to_search == number_list[i]:
            indices.append(i)
        else:
            break
        i += 1
        
    return sorted(indices)


print(find_all_occurrences([1,4,6,9,11,15,15,15,17,21,34,34,56], 56))
