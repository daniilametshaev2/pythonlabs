# Открываем файл input.txt для чтения
with open('1input.txt', 'r') as infile:
    line = infile.read()  # читаем всю строку

# Разбиваем строку по пробелам и преобразуем в числа
numbers = list(map(int, line.split()))

# Проверка: убедимся, что у нас 10 чисел
if len(numbers) != 10:
    print("В файле должно быть ровно 10 чисел.")
else:
    # Вычисляем произведение всех чисел
    product = 1
    for num in numbers:
        product *= num

    # Записываем результат в output.txt
    with open('1output.txt', 'w') as outfile:
        outfile.write(str(product))
