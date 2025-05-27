text ="""3,4,17,-3
5,11,-1,6
0,2,-5,8"""
filename = "matrix.txt"
with open(filename, "w") as file:
    file.write(text)

matrix = []
with open(filename, "r") as file:
    for line in file:
        line = line.strip()
        row = list(map(int, line.split(',')))
        matrix.append(row)

total_sum = sum(sum(row) for row in matrix)
max_element = max(max(row) for row in matrix)
min_element = min(min(row) for row in matrix)

print(f"Сумма всех элементов: {total_sum}")
print(f"Максимальный элемент: {max_element}")
print(f"Минимальный элемент: {min_element}")
