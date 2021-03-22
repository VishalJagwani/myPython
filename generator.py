# def gen_func(num):
#     for i in range(num):
#         yield i*2


# g = gen_func(100)
# next(g)
# next(g)
# print(next(g))

# print(next(g))
class MyGen():
    curr = 0

    def __init__(self,  first, last):
        self.first = first
        self.last = last

    def __iter__(self):
        return self

    def __next__(self):
        if MyGen.curr < self.last:
            num = MyGen.curr
            MyGen.curr += 1
            return num
        raise StopIteration


gen = MyGen(0, 100)
for i in gen:
    print(i)
