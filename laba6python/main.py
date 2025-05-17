import json
import csv
import os
import sys

# Подставляем аргумент вручную (если не запускаешь из терминала)
sys.argv = ["json2csv.py", "Sample-employee-JSON-data.json"]

def json_to_csv(json_path):
    if not os.path.exists(json_path):
        print(f"Файл не найден: {json_path}")
        return

    base_name = os.path.splitext(os.path.basename(json_path))[0]
    folder = os.path.dirname(json_path)
    csv_path = os.path.join(folder, base_name + ".csv")

    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    if isinstance(data, list):
        if len(data) == 0:
            print("JSON-файл пуст.")
            return
        keys = data[0].keys()
        with open(csv_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(data)
    elif isinstance(data, dict):
        for value in data.values():
            if isinstance(value, list) and all(isinstance(i, dict) for i in value):
                keys = value[0].keys()
                with open(csv_path, 'w', newline='', encoding='utf-8') as f:
                    writer = csv.DictWriter(f, fieldnames=keys)
                    writer.writeheader()
                    writer.writerows(value)
                break
        else:
            print("Не удалось найти список словарей в JSON.")
            return
    else:
        print("Неподдерживаемый формат JSON.")
        return

    print(f"✅ CSV-файл успешно сохранён: {csv_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Использование: python json2csv.py <файл.json>")
    else:
        json_file = sys.argv[1]
        json_to_csv(json_file)
