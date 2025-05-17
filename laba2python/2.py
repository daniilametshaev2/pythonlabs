def trisimv(s):
    s = s.replace(" ", "")
    char_count = {}
    
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
            
    count_list = [(char, count) for char, count in char_count.items()]
    count_list.sort(key=lambda x: x[1], reverse=True)
    return count_list[:3]

input_string = input("vvedite stroku: ")
common_characters = trisimv(input_string)

print("3 naibolee vstr simvola:")
for char, count in common_characters:
    print(f"'{char}': {count}")