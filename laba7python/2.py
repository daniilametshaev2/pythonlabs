import json

with open('ex_2.json', 'r', encoding='utf-8') as f:
    content = f.read()

# Добавляем квадратные скобочки
# Для этого разделим по '}{' и вставим '},{'
objects = content.strip().replace('}{', '},{')
json_array_str = f'[{objects}]'

data = json.loads(json_array_str)

with open('new_ex_2.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

users_dict = {user['name']: user['phoneNumber'] for user in data}

# Вывести словарь
print(users_dict)
