import json
person = {'name': 'Max', 'age': 10, 'phones': ['9111', '738333']}
result = json.dumps(person)
print(result)
print(type(result))

spisok = (12, 25, 'яблоко', 'день')
result1 = json.dumps(spisok)
print(result1)
print(type(result1))

