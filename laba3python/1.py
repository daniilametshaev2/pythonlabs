def swap_min_max(numbers):
    if not numbers:
        return numbers
    min_index = numbers.index(min(numbers))
    max_index = numbers.index(max(numbers))
    numbers[min_index], numbers[max_index] = numbers[max_index], numbers[min_index]

    return numbers

input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print(input_list)
output_list = swap_min_max(input_list)
print(output_list) 
