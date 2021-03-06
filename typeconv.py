import datetime

birth_year = input('What year you were born?')

x = datetime.datetime.now()
age = x.year - int(birth_year)

print('Your age is ' + str(age))
