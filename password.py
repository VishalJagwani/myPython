username = input('Enter username: ')
password = input('Enter password: ')

password_length = len(password)
starred = '*' * len(password)

print(f'{username}, your password {starred} is {password_length} letters long')
# print(f'{username}, your password {starred} is {len(password)} letters long')
