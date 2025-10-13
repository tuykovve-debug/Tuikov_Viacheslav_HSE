import json

purchases = {}

with open('purchase_log.txt', 'r', encoding='utf-8') as file:
    for line in file:
        data = json.loads(line.strip())
        user_id = data['user_id']
        category = data['category']
        print(f"{user_id} ‘{category}‘")