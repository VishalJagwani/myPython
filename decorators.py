# have @ symbol Ex. @classmethod, @staticmethod
# Higher Order Function
# def greet(hello):  # Function in function
#     def hello():
#         return 0
#     return hello()
# Examples map, filter, reduce, zip
# Function that wraps another function and super boosts our function : Decorator

def my_decorator(func):
    def my_wrap_func(*args, **kwargs):
        print('************')
        func(*args, **kwargs)
        print('************')
    return my_wrap_func


@my_decorator
def hello(greet, emoji=':)'):
    print(greet, emoji)


@my_decorator
def bye():
    print('See ya later')


hello('Hii')
bye()
