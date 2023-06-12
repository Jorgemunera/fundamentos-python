person = {
    'name': 'Nicolas',
    'lastName': 'Molina',
    'age': 29
}

person['twitter'] = '@nicobytes'

person['name'] = 'Felipe'

del person['age']

print(person.keys())
print(person.values())