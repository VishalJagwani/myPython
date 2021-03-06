basket = [1, 2, 3, 4, 5]
print(len(basket))  # 5

# adding
basket.append(100)  # add to end
basket.insert(6, 200)
basket.extend([201])  # extends list
print(basket)

# removing
basket.pop(7)  # 7th item ....Index
basket.remove(5)  # Value 5 .....Value
basket.clear()  # Empty list returned
print(basket)

new_basket = ['a', 'x', 'b', 'c', 'd', 'e', 'd']
print(new_basket.index('d', 0, 6))  # list.index(value, start, stop)

print('d' in new_basket)  # True
print(new_basket.count('d'))  # How many times it occurs

# new_basket.sort()
# new list created as new_list = new_basket[:] and new_list.sort()
print(sorted(new_basket))
print(new_basket)

# new_list = new_basket[:] is same as new_list = new_basket.copy()
new_basket.sort()
new_basket.reverse()  # only reverse
print(new_basket)  # sorted and reversed
print(new_basket[::-1])  # new list
print(new_basket)

print(list(range(101)))  # 0 to 100
print(list(range(1, 100)))  # 1 to 99

sentence = ' '.join(['hi', 'my', 'name', 'is', 'StarVJ'])
print(sentence)

# List unpacking
a, b, c, *other, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)  # 1
print(b)  # 2
print(c)  # 3
print(other)  # [4,5,6,7,8]
print(d)  # 9
