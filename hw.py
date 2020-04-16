from random import randint


def create_the_board(rows, columns):
    li = []
    for r in range(rows):
        li.append([])
        for c in range(columns):
            if r == 0:
                li[r].append(str(c) + "  ") if c < 1 else li[r].append(str(c) + " ")
            elif c == 0 and r != 0:
                li[r].append(str(r) + "  ") if r < 10 else li[r].append(str(r) + " ")
            else:
                li[r].append("? ") if c < 10 else li[r].append("?  ")
    return li


def get_coordinates_of_duality_ship():
    """

    :return: [[point_1_x, point_1_y], [point_2_x, point_2_y]]
    """

    # Create a random x and y for the first point
    point_1_x = randint(1, row - 1)
    point_1_y = randint(1, column - 1)

    # The first point
    first_point = [point_1_x, point_1_y]

    # THE SECOND POINT
    # the allowed points for the second point of the second ship
    # We don't want some points to be crossed. so, now we   have
    # 4 allowed points we will take one randomly.
    temp = [
            [point_1_x - 1, point_1_y],
            [point_1_x, point_1_y - 1],
            [point_1_x, point_1_y + 1],
            [point_1_x + 1, point_1_y]
    ]

    k = randint(0, 3)  # Generate a key for the random point.
    point_2_x = temp[k][0]  # x of the random point.
    point_2_y = temp[k][1]  # y of the random point.

    # Don't let the point sit on the borders
    while point_2_x == 0 or point_2_y == 0 or point_2_x == row or point_2_y == column:
        k = randint(0, 3)  # Generate a new key for the NEW random point
        point_2_x = temp[k][0]
        point_2_y = temp[k][1]

    # The second point
    second_point = [point_2_x, point_2_y]

    # The coordinates of the duality ship
    return [first_point, second_point]


def draw_the_second_ship(table):
    """

    :param table: board list
    :return: NoneType
    """

    # [[point_1_x, point_1_y], [point_2_x, point_2_y]]
    ship = get_coordinates_of_duality_ship()
    table[ship[0][0]][ship[0][1]] = "\033[93mX\033[0m "
    table[ship[1][0]][ship[1][1]] = "\033[93mX\033[0m "


row, column = 6, 6
board = create_the_board(row, column)

draw_the_second_ship(board)

for i in board:
    for x in i:
        print(x, end="")

    print()
