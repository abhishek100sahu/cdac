from time_counter import time_counter


@time_counter
def linear_search(numbers_list, number_to_find):
    for i in range(len(numbers_list) - 1):
        if numbers_list[i] == number_to_find:
            return i
    return -1


@time_counter
def binary_search(numbers_list, number_to_find):
    left_index = 0
    right_index = len(numbers_list) - 1
    mid_index = 0

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = numbers_list[mid_index]

        if mid_number == number_to_find:
            return mid_index

        if mid_number < number_to_find:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1

    return -1


@time_counter
def binary_search_recursive(numbers_list, number_to_search, left_index, right_index):
    if right_index < left_index:
        return -1

    mid_index = (left_index + right_index) // 2

    if numbers_list[mid_index] == number_to_search:
        return mid_index

    if numbers_list[mid_index] < number_to_search:
        left_index = mid_index + 1

    else:
        right_index = mid_index - 1

    return binary_search_recursive(
        numbers_list, number_to_search, left_index, right_index
    )


print(binary_search([i for i in range(100000)], 255))

print(linear_search([i for i in range(100000)], 255))

print(
    binary_search_recursive(
        [i for i in range(100000)], 255, 0, len([i for i in range(100000)])
    )
)
