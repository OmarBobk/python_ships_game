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


def get_coordinates_of_unity_ship():
    """
        :return: [x, y]
    """

    # Create a random x and y for point
    point_x = randint(1, row - 1)
    point_y = randint(1, column - 1)

    # The coordinates of the unity ship
    return [point_x, point_y]


def draw_the_unity_ship(table, recursion_counter=0):
    """
    :param recursion_counter:
    :param table: board list
    :return: Boolean
    """

    # [point_x, point_y]
    ship = get_coordinates_of_unity_ship()

    point_x = ship[0]
    point_y = ship[1]

    if "X" not in table[point_x][point_y]:
        table[point_x][point_y] = "\033[93mX\033[0m "
        return True
    else:
        return False if recursion_counter > 10 else draw_the_unity_ship(table, recursion_counter+1)


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


def draw_the_duality_ship(table, recursion_counter=0):
    """
    :param recursion_counter:
    :param table: board list
    :return: Boolean
    """
    # [[point_1_x, point_1_y], [point_2_x, point_2_y]]
    ship = get_coordinates_of_duality_ship()

    point_1_x = ship[0][0]
    point_1_y = ship[0][1]
    point_2_x = ship[1][0]
    point_2_y = ship[1][1]

    # Check if there is no ships in this coordinates
    if "X" not in table[point_1_x][point_1_y] and "X" not in table[point_2_x][point_2_y]:
        table[point_1_x][point_1_y] = "\033[93mX\033[0m "
        table[point_2_x][point_2_y] = "\033[93mX\033[0m "

        return True
    else:
        return False if recursion_counter > 10 else draw_the_duality_ship(table, recursion_counter+1)


def get_coordinates_of_trinity_ship():
    """
        :return: [[point_1_x, point_1_y], [point_2_x, point_2_y], [point_3_x, point_3_y]]
    """
    # [[point_1_x, point_1_y], [point_2_x, point_2_y]]
    duality = get_coordinates_of_duality_ship()
    x = duality[1][0]  # 3
    y = duality[1][1]  # 3

    allowed_points = [
        [x+1, y],  # 4, 3
        [x-2, y],  # 1, 3
        [x-1, y],  # 2, 3
        [x+2, y],  # 5, 3
        [x, y+1],  # 3, 4
        [x, y-2],  # 3, 1
        [x, y-1],  # 3, 2
        [x, y+2],  # 3, 5
    ]

    allowed_points_key = randint(0, 7)
    z = [allowed_points[allowed_points_key][0],
         allowed_points[allowed_points_key][1]]

    print(duality)
    print(allowed_points_key)
    print("--------")
    print([x, y], z)
    print("--------")


row, column = 6, 6
board = create_the_board(row, column)

get_coordinates_of_trinity_ship()

for i in board:
    for x in i:
        print(x, end="")

    print()


