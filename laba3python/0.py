def greater_than_previous(numbers):
    result = []

    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i - 1]:
            result.append(numbers[i]) 
    
    return result
input_list = [5,6,8,1,3,2,4]
output_list = greater_than_previous(input_list)
print(output_list)