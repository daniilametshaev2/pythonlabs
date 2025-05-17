def countnumbers(list1, list2):
    same = 0

    for number in list1:
        if number in list2:
            same += 1
            
    return same
input_list1 = [1, 2, 3, 4, 5]
input_list2 = [4, 5, 6, 7, 8]
same = countnumbers(input_list1, input_list2)
print(same) 