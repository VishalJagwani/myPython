picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]


for row in picture:
    for pixel in row:
        if pixel:
            print('*', end="")
        else:
            print(' ', end="")
    print('')

# end="" is for not wanting new line for every print
# inner for has print('') to have new line for every row
