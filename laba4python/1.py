# Задаем словарь
my_dict = {'Hello' : 'Hi', 'Bye' : 'Goodbye', 'List' : 'Array'}

# Запрашиваем ключ у пользователя
key = input()

# Выводим значение по ключу, если он есть в словаре
print(my_dict.get(key))
