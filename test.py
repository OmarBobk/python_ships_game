from random import randint


class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


w = 10  # int(input("Enter number of columns: "))
h = 10  # int(input("Enter number of rows: "))

u_row = randint(1, h)
u_column = randint(1, w)

d_row = randint(1, h)
d_column = randint(1, w)

if d_column == w:
    d_column = d_column - 1

unity = [u_row, u_column]
duality = [d_row, d_column]
trinity = [3, 3]
quatrain = [4, 4]

ships = [unity, [2, 2], trinity, quatrain]

x = ships[1][1] + 1
x_1 = ships[1][1] - 1

x_2 = ships[1][0] + 1
x_3 = ships[1][0] - 1

x_list = [x, x_1]
y_list = [x_2, x_3]

for row in range(h + 1):
    for column in range(w):
        if column == 0:
            print(row, "" if row > 9 or row == 0 else " ", end="")
        if row == 0:
            if column == 0:
                print(" ", end="")
            print(column + 1, "", end="")
        else:
            if row == ships[0][0] and column + 1 == ships[0][1]:
                print("\033[93mX\033[0m", end=" ")
            elif row == ships[1][0] and column + 1 == ships[1][1]:
                print("\033[93mX\033[0m", end=" ")
            elif row == ships[1][0] + 1 and column + 1 == ships[1][1]:
                print("\033[93mX\033[0m", end=" ")
            else:
                print("?", end=" ")
            if column > 9:
                print(" ", end="")

    print()

# column_guess = input("Guess Column: ")
# row_guess = input("Guess Row: ")


# ships = [unity, duality, trinity, quatrain]
