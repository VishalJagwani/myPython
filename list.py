amazon_cart = ['Macbook', 'iPhone', 'Mango', 'IceCream']
# List slicing

amazon_cart[3] = 'Cornetto'  # list are mutable Strings are not

print(amazon_cart[1:3])  # list[start at : end before]

# new_cart = amazon_cart Means new_cart will refer to same memory where amazon_cart is located
# new_cart = amazon_cart[:] This is copying to new_cart
new_cart = amazon_cart[0:3]
new_cart[0] = 'HpNotebook'

print(new_cart)

print(amazon_cart)

# Matrix
matrix = [
    [1, 5, 1],
    [0, 1, 0],
    [1, 0, 1]
]

print(matrix[0][1])  # matrix[First_Element][Second Value]
