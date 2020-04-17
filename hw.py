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


def is_vertically(duality_ship):
    """
    Check if the given duality ship is vertically or horizontally
    :type duality_ship: [[point_1_x, point_1_y], [point_2_x, point_2_y]]
    :return: Boolean
    """

    # The first point x
    point_1_x = duality_ship[0][0]

    # The second point x
    point_2_x = duality_ship[1][0]

    return False if point_1_x == point_2_x else True


def is_empty_list(li):
    """
    Check if the given list is empty or not
    :param li:
    :return: Boolean
    """
    if len(li) == 0:
        return True
    else:
        return False


def rest_of_list(li):
    """
    Remove the first item of the given list and return it
    :param li: list [[point_x_1, point_y_1], [point_x_2, point_y_2], ...]
    :return: list
    """
    ship = li.copy()
    ship.remove(ship[0])
    return ship


def get_allowed_point(allowed_points, cases):
    """

    :param allowed_points: list of list of ints [[point_x_1, point_y_1], [point_x_2, point_y_2], ...]
    :param cases: int number of lists inside allowed_points
    :return: list of ints [int, int]
    """
    allowed_points_key = randint(0, cases)

    point_x = allowed_points[allowed_points_key][0]
    point_y = allowed_points[allowed_points_key][1]
    # Don't let the point sit on the borders
    while point_x == 0 or point_y == 0 or point_x == row or point_y == column:
        allowed_points_key = randint(0, 1)  # Generate a new key for the NEW random point
        point_x = allowed_points[allowed_points_key][0]
        point_y = allowed_points[allowed_points_key][1]

    return [point_x, point_y]


def get_coordinates_of_unity_ship():
    """
        :return: list of lists of ints [x, y]
    """

    # Create a random x and y for point
    point_x = randint(1, row - 1)
    point_y = randint(1, column - 1)

    # The coordinates of the unity ship
    return [[point_x, point_y]]


def get_coordinates_of_duality_ship():
    """
    :return: [[point_1_x, point_1_y], [point_2_x, point_2_y]]
    """

    # The first point
    # [[point_1_x, point_1_y]]
    first_point = get_coordinates_of_unity_ship()

    # allowed points for second point
    allowed_points = [
        [first_point[0][0], first_point[0][1] + 1],
        [first_point[0][0] + 1, first_point[0][1]]
    ]

    # The second point
    second_point = get_allowed_point(allowed_points, 1)  # [point_x, point_y]
    # The coordinates of the duality ship
    return [first_point[0], second_point]


def get_coordinates_of_trinity_ship():
    """
        :return: [[point_1_x, point_1_y], [point_2_x, point_2_y], [point_3_x, point_3_y]]
    """
    duality = get_coordinates_of_duality_ship()

    if is_vertically(duality):
        allowed_points = [
            [duality[1][0] + 1, duality[1][1]],
            [duality[1][0] - 2, duality[1][1]],
        ]
    else:
        allowed_points = [
            [duality[1][0], duality[1][1] + 1],
            [duality[1][0], duality[1][1] - 2],
        ]

    return [
        [duality[0][0], duality[0][1]],
        [duality[1][0], duality[1][1]],
        get_allowed_point(allowed_points, 1)
    ]


def get_coordinates(which_ship):
    """
    :type which_ship: int
    """
    if which_ship == 1:
        return get_coordinates_of_unity_ship()
    elif which_ship == 2:
        return get_coordinates_of_duality_ship()
    elif which_ship == 3:
        return get_coordinates_of_trinity_ship()


def draw_the_ship(table, ship, which_ship, recursion_counter=0):
    """
    :param which_ship: 2
    :param ship: # [[point_x, point_y]]
    :param recursion_counter:
    :param table: board list
    :return: Boolean
    """

    new_ship = get_coordinates(which_ship)

    if is_empty_list(ship):
        return True
    else:
        if "X" not in table[ship[0][0]][ship[0][1]] and draw_the_ship(table, rest_of_list(ship), which_ship):
            table[ship[0][0]][ship[0][1]] = "\033[93mX\033[0m "
            return True
        else:
            return False if recursion_counter > 10 else draw_the_ship(table, new_ship, which_ship, recursion_counter+1)


row, column = 11, 11
board = create_the_board(row, column)

draw_the_ship(board, get_coordinates(1), 1)  # the first ship
draw_the_ship(board, get_coordinates(2), 2)  # the second ship
draw_the_ship(board, get_coordinates(3), 3)  # the third ship


for i in board:
    for x in i:
        print(x, end="")

    print()

