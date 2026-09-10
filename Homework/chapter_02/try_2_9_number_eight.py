# try_2_9_number_eight.py
DRAW_LENGTH = 20
def line(DRAW_LENGTH):
    for i in range(DRAW_LENGTH):
        print("-", end="")
    print()  # Move to the next line after drawing the line
'''def btm_line(DRAW_LENGTH):
    for i in range(DRAW_LENGTH):
        print("-", end="")
    print()  # Move to the next line after drawing the line'''


# btm_line(DRAW_LENGTH)
def line_type2 (DRAW_LENGTH):
    i = 0
    while i < DRAW_LENGTH:
        print("-", end="")
        i += 1
    print()  # Move to the next line after drawing the line
line_type2(DRAW_LENGTH)
print(4 + 4)
line_type2(DRAW_LENGTH)
print(12 - 4)
line(DRAW_LENGTH)
print(4 * 2)
line(DRAW_LENGTH)
print(8 / 1)
line(DRAW_LENGTH)
print('EXTRA CREDIT')
line(DRAW_LENGTH)
print((8 / 8) * (4 + 4))
line(DRAW_LENGTH)
print(-4 + 8 + 2 * 2) # Returns 8 as the result of the expression is an integer
line(DRAW_LENGTH)
print(-4 + 8 + 8 / 2) # Returns 8.0 as the result of the expression is a float
line(DRAW_LENGTH)