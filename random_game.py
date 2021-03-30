from random import randint
# import sys
answer = randint(1, 10)
# answer = randint(sys.argv[1], sys.argv[2]) # For terminal input

while True:
    try:
        guess = int(input('Guess a number 1~10:  '))
        if 0 < guess < 11:
            if guess == answer:
                print('Awesome, that is correct!')
                break
        else:
            print('Guess between 1~10 ONLY')
    except ValueError:
        print('Please enter a number')
        continue
