# used with list, set, dict

# Quicker way than for loop
my_list = [char for char in 'hello']
my_list2 = [num for num in range(0, 101)]
my_list3 = [num**2 for num in range(0, 101)]
my_list4 = [num**2 for num in range(0, 101) if num % 2 == 0]

# For set comprehension replace [] by {}

# for char in 'hello':
#     my_list.append(char)

# print(my_list4)

# Dict comprehension

simple_dict = {
    'a': 1,
    'b': 2
}

my_dict = {key: value**2 for key, value in simple_dict.items() if value %
           2 == 0}
# print(my_dict)
my_dict2 = {num: num*2 for num in [1, 2, 3]}
# print(my_dict2)

# Exercise
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = list(set([x for x in some_list if some_list.count(x) > 1]))
print(duplicates)
