# map, filter, zip, reduce
# functional(action/function, data)
from functools import reduce


def mult_by2(i):  # li was in ()
    # new_li = []
    # for i in li:
    #     new_li.append(i * 2)
    # return new_li
    return i*2


def only_odd(item):
    return item % 2 != 0


def accumulator(acc, item1):
    print(acc, item1)
    return acc + item1


# print(list(map(mult_by2, [1, 2, 3])))
# print(list(map(lambda i1: i1*2, [1, 2, 3]))) to use function only once
# Similarly filter, reduce with lambda
# print(list(filter(only_odd, [1, 2, 3])))
# print(list(zip([1, 2, 3], [10, 20, 30])))
# print(reduce(accumulator, [1, 2, 3], 0))

# exercise
list1 = [5, 4, 3]
new_list = list(map(lambda num: num**2, list1))
print(new_list)

a = [(0, 2), (4, 3), (10, -1), (9, 9)]
a.sort(key=lambda x: x[1])  # To sort by 2nd value in tuple
print(a)
