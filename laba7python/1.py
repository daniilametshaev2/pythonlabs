import json
from jsonschema import validate, ValidationError
from schema import schema 

#'invalid_ex_1.json' для проверки ошибки
filename = 'ex_1.json'

with open(filename, 'r') as file:
    data = json.load(file)

try:
    validate(instance=data, schema=schema)
    print("JSON корректен. Валидация прошла успешно.")
except ValidationError as e:
    print("Ошибка валидации:")
    print(e.message)
