is_old = True
is_licenced = True

if is_old and is_licenced:
    print('You are old enough to drive, You can drive now')
else:
    print('check')

# Truthy and Falsy
# All values are considered "truthy" except for the following, which are "falsy":

# None
# False
# 0
# 0.0
# 0j
# Decimal(0)
# Fraction(0, 1)
# [] - an empty list
# {} - an empty dict
# () - an empty tuple
# '' - an empty str
# b'' - an empty bytes
# set() - an empty set
# an empty range, like range(0)
# objects for which
# obj.__bool__() returns False
# obj.__len__() returns 0
# A "truthy" value will satisfy the check performed by if or while statements. We use "truthy" and "falsy" to differentiate from the bool values True and False.

# Ternary Operator
is_friend = False
can_message = 'Message Allowed' if is_friend else 'Not allowed'
print(can_message)
# Short Circuiting
if is_old or is_licenced:
    print('Driving allowed')
# If one of the condition is true it short circuit the next and print
