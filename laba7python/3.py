import json

with open('ex_3.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

new_invoice = {
    "id": 3,
    "total": 150.00,
    "items": [
        {
            "name": "item 4",
            "quantity": 3,
            "price": 50.00
        }
    ]
}

data['invoices'].append(new_invoice)
with open('updated_3.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
