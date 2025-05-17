with open('2input.txt', 'r') as infile:
    numbers = [int(line.strip()) for line in infile]

# Сортируем по возрастанию чисел
numbers_sorted = sorted(numbers)

with open('2output.txt', 'w') as outfile:
    for num in numbers_sorted:
        outfile.write(str(num) + '\n')
