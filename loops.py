# Strings, List, Sets, Tuple can be used in for loop
# for item in [1, 2, 3, 4, 5]:
#     for x in ['a', 'b', 'c']:
#         print(item, x)

# Iterable : list, dictionary, tuple, sets, Strings
# iterated -> one by one check each item in collection

# user = {
#     'name': 'Wizard',
#     'age': 22,
#     'can_fly': False
# }

# # for item in user.items():
# for key, value in user.items():
#     print(key, value)

# for item in user.values():
#     print(item)

# for item in user.keys():
#     print(item)

# counter
# my_list = [1, 2, 3, 4, 5, 6, 8, 7, 9, 10]

# counter = 0
# for item in my_list:
#     counter = counter + item
# print(counter)

# for i in range(2):
#     print(list(range(10)))

# for i, char in enumerate(list(range(100))):
#     # print(i, char)
#     if char == 50:
#         print(f'Index of 50 is {i}')

# i = 0
# while i < 10:
#     print(i)
#     i += 1
#     # break
# else:
#     print('Done')
while True:
    response = input('Say something : ')
    if response == 'bye':
        break

#  break, continue, pass
