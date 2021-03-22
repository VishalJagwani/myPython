while True:
    try:
        age = int(input('What is your age?'))
        10/age
        # print(age)
        # raise ValueError('Hey cut it out')
        # raise Exception('Hey cut it out')
    # except ValueError:
    #     print('Please Enter a Number.')
    #     continue
    except ZeroDivisionError:
        print('Please Enter a Number greater than 0.')
        break
    else:
        print('Thank You!')
    finally:
        print('Done for now')
    print('Can you hear me?')
# def sum1(n1, n2):
#     try:
#         return n1/n2
#     except (TypeError, ZeroDivisionError) as err:
#         print(err)


# print(sum1(1, '0'))
