# Method Resolution Operator
class A():
    num = 10


class B(A):
    pass


class C(A):
    num = 1


class D(B, C):
    pass


print(D.num)  # Gives 1 as Order is D-B-C-A and not D-B-A
# print(D.mro()) Gives Order it'll be checked in
# print(D.__mro__) is also same
