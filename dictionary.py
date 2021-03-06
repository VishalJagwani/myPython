# Dictionary
dictionary = {
    'a': 1,
    'b': 'Hello',
    'c': True
}
# Unordered key : value pairs
# print(dictionary['b'])  # Accessing value using key b

my_list = [
    {
        'a': [1, 2, 3],
        'b': 2,
        'c':True
    },
    {
        'a': 'Hello',
        'b': 115,
        'c': True
    }
]
# print(my_list[1]['a'])
# Dictionary keys need to be immutable, List can't be used as keys
# Unique keys otherwise overwritten

# print(dictionary.get('b', 4))  # get value of b if doesn't exists return 4

user = dict(name='StarVJ')
# print(user)
# print('name' in user)
# print('b' in dictionary.keys())
# print(1 in dictionary.values())
# print(dictionary.items())
# print(user)
# user.clear()
# print(user)

# user2 = user.copy()
# print(user2)

# print(dictionary.pop('c'))
# print(dictionary.popitem())
# print(dictionary)

print(dictionary.update({'c': False}))
print(dictionary.update({'c1': False}))
print(dictionary)
