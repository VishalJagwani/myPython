from collections import Counter, defaultdict, OrderedDict

li = [1, 2, 3, 4, 5, 6, 7, 7]
# print(Counter(li))

sentence = 'blah blah blah thinking about love'
# print(Counter(sentence))

dictionary = defaultdict(lambda: 'does not exist', {'a': 1, 'b': 2})
# print(dictionary['c'])

d1 = OrderedDict()
d1['a'] = 1
d1['b'] = 2

d2 = OrderedDict()
# d2['b'] = 2  False Bcoz order of insertion is not same
d2['a'] = 1  # True
d2['b'] = 2

print(d2 == d1)
