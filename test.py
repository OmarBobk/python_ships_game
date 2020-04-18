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
    :param li: list
    :return: Boolean
    """
    if type(li) == list:
        if len(li) == 0:
            return True
        else:
            return False
    else:
        print("The given argument ({}) is not a list".format(li))


def rest_of_list(li):
    """
    Remove the first item of the given list and return it
    :param li: list [[point_x_1, point_y_1], [point_x_2, point_y_2], ...]
    :return: list
    """
    if is_empty_list(li):
        return []
    else:
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
    while point_x == 0 or point_y == 0:
        allowed_points_key = randint(0, 1)  # Generate a new key for the NEW random point
        point_x = allowed_points[allowed_points_key][0]
        point_y = allowed_points[allowed_points_key][1]

    return [point_x, point_y, allowed_points_key]


def get_coordinates_of_unity_ship(table, recursion_counter=0):
    """
        :return: list of lists of ints [x, y]
    """

    # Create a random x and y for point
    point_x = randint(1, row - 1)
    point_y = randint(1, column - 1)

    # The coordinates of the unity ship
    if table[point_x][point_y][0] == "?":
        table[point_x][point_y] = "\033[93mX\033[0m "
        return [[point_x, point_y]]
    else:
        return False if recursion_counter > 10 else get_coordinates_of_unity_ship(table, recursion_counter + 1)


def get_coordinates_of_duality_ship(table, recursion_counter=0):
    """
    :return: [[point_1_x, point_1_y], [point_2_x, point_2_y]]
    """
    omar = ""
    # The first point
    # [[point_1_x, point_1_y]]
    # [2, 5]
    first_point = get_coordinates_of_unity_ship(table)

    if first_point[0][0] == row - 1 and first_point[0][1] == column - 1:
        cases = 1
        flag = "a"
        # allowed points for second point
        allowed_points = [
            [first_point[0][0], first_point[0][1] - 1],
            [first_point[0][0] - 1, first_point[0][1]],
        ]
    elif first_point[0][0] == row - 1:
        cases = 2
        flag = "b"
        # allowed points for second point
        allowed_points = [
            [first_point[0][0], first_point[0][1] + 1],
            [first_point[0][0], first_point[0][1] - 1],
            [first_point[0][0] - 1, first_point[0][1]],
        ]
    elif first_point[0][1] == column - 1:
        cases = 2
        flag = "c"
        # allowed points for second point
        allowed_points = [
            [first_point[0][0], first_point[0][1] - 1],
            [first_point[0][0] - 1, first_point[0][1]],
            [first_point[0][0] + 1, first_point[0][1]],
        ]
    else:
        cases = 3
        flag = "d"
        # allowed points for second point
        allowed_points = [
            [first_point[0][0], first_point[0][1] - 1],
            [first_point[0][0], first_point[0][1] + 1],
            [first_point[0][0] - 1, first_point[0][1]],
            [first_point[0][0] + 1, first_point[0][1]],
        ]

    # The second point
    second_point = get_allowed_point(allowed_points, cases)  # [point_2_x, point_2_y, allowed_points_key]
    allowed_key_point = second_point[2]
    if flag == "a":
        if allowed_key_point == 0:
            omar = "x, y-1"
        elif allowed_key_point == 1:
            omar = "x-1, y"
    elif flag == "b":
        if allowed_key_point == 0:
            omar = "x, y+1"
        elif allowed_key_point == 1:
            omar = "x, y-1"
        elif allowed_key_point == 2:
            omar = "x-1, y"
    elif flag == "c":
        if allowed_key_point == 0:
            omar = "x, y-1"
        elif allowed_key_point == 1:
            omar = "x-1, y"
        elif allowed_key_point == 2:
            omar = "x+1, y"
    elif flag == "d":
        if allowed_key_point == 0:
            omar = "x, y-1"
        elif allowed_key_point == 1:
            omar = "x, y+1"
        elif allowed_key_point == 2:
            omar = "x-1, y"
        elif allowed_key_point == 3:
            omar = "x+1, y"

    # The coordinates of the duality ship
    # [[point_1_x, point_1_y], [point_2_x, point_2_y]]
    ship = [first_point[0], [second_point[0], second_point[1]], omar]

    if table[ship[0][0]][ship[0][1]][0] == "?" and table[ship[1][0]][ship[1][1]][0] == "?":
        table[ship[0][0]][ship[0][1]] = "\033[93mX\033[0m "
        table[ship[1][0]][ship[1][1]] = "\033[93mX\033[0m "

        return ship
    else:
        return False if recursion_counter > 10 else get_coordinates_of_duality_ship(table, recursion_counter + 1)


def get_coordinates_of_trinity_ship(table, recursion_counter=0):
    """
        :param table: list
        :type recursion_counter: int
        :return: [[point_1_x, point_1_y], [point_2_x, point_2_y], [point_3_x, point_3_y]]
    """
    # Draw the first tow points and return them coordinates
    # [[point_1_x, point_1_y], [point_2_x, point_2_y], omar]
    duality = get_coordinates_of_duality_ship(table)
    x = duality[0][0]
    y = duality[0][1]
    # if y+1: use y+2 or y-1
    # if y-1: use y-2 or y+1
    # if x+1: use x+2 or x-1
    # if x-1: use x-2 or x+1
    omar = duality[2]
    if omar == "x, y+1":
        if y == column-2:
            cases = 0
            allowed_points = [
                [x, y - 1]
            ]
        else:
            cases = 1
            allowed_points = [
                [x, y+2],
                [x, y-1]
            ]

    elif omar == "x, y-1":
        if y == column-1:
            cases = 0
            allowed_points = [
                [x, y - 2]
            ]
        else:
            cases = 1
            allowed_points = [
                [x, y - 2],
                [x, y + 1]
            ]
    elif omar == "x+1, y":
        if x == row-2:
            cases = 0
            allowed_points = [
                [x - 1, y]
            ]
        else:
            cases = 1
            allowed_points = [
                [x + 2, y],
                [x - 1, y]
            ]

    elif omar == "x-1, y":
        if x == row-1:
            cases = 0
            allowed_points = [
                [x - 2, y]
            ]
        else:
            cases = 1
            allowed_points = [
                [x + 1, y],
                [x - 2, y]
            ]

    else:
        cases = 0
        allowed_points = ["if you are seeing this message then you need to know that "
                          "there is an Error that only god know what is it "]

    # [point_x, point_y, allowed_points_key]
    allowed_point = get_allowed_point(allowed_points, cases)
    third_point = [allowed_point[0], allowed_point[1]]
    ship = [duality[0], duality[1], third_point]
    print(ship)
    print(allowed_point[2])
    print(omar)
    if table[third_point[0]][third_point[1]][0] == "?":
        table[third_point[0]][third_point[1]] = "\033[93mX\033[0m "


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


def draw_the_unity_ship(table, recursion_counter=0):
    # [[point_x, point_y]]
    ship = get_coordinates_of_unity_ship()

    if table[ship[0][0]][ship[0][1]][0] == "?":
        table[ship[0][0]][ship[0][1]] = "\033[93mX\033[0m "
        return True
    else:
        return False if recursion_counter > 10 else draw_the_unity_ship(table, recursion_counter+1)


def draw_the_ship(table, ship, which_ship, recursion_counter=0):
    """
    :param which_ship: int
    :param ship: # list [[point_x, point_y]]
    :param recursion_counter:
    :param table: board list
    :return: Boolean
    """
    if is_empty_list(ship):
        return True
    else:
        if table[ship[0][0]][ship[0][1]][0] == "?" and draw_the_ship(table, rest_of_list(ship), which_ship):
            table[ship[0][0]][ship[0][1]] = "\033[93mX\033[0m "
            return True
        else:
            return False if recursion_counter > 10 else draw_the_ship(table, get_coordinates(which_ship), which_ship,
                                                                      recursion_counter + 1)


row, column = 4, 4
board = create_the_board(row, column)


get_coordinates_of_unity_ship(board)
get_coordinates_of_duality_ship(board)
get_coordinates_of_trinity_ship(board)

for i in board:
    for x in i:
        print(x, end="")

    print()

