"""
Daily Coding Problem - 2018-11-15.

Conway's Game of Life takes place on an infinite two-dimensional board
of square cells. Each cell is either dead or alive, and at each tick,
the following rules apply:
    Any live cell with less than two live neighbours dies.
    Any live cell with two or three live neighbours remains living.
    Any live cell with more than three live neighbours dies.
    Any dead cell with exactly three live neighbours becomes a live cell.
    A cell neighbours another cell if it is horizontally, vertically,
        or diagonally adjacent.

Implement Conway's Game of Life. It should be able to be initialized
with a starting list of live cell coordinates and the number of steps it
should run for. Once initialized, it should print out the board state at
each step. Since it's an infinite board, print out only the relevant
coordinates, i.e. from the top-leftmost live cell to bottom-rightmost
live cell.

Represent a live cell with an asterisk (*) and a dead cell with a dot (.).
"""


def simulate(live_coords=None, steps=0, bounds=None):
    """Simulate Conway's Game."""
    if live_coords is None:
        print('--- game over: nothing alive ---')
        return True
    if not steps:
        print('--- game over: no steps remain ---')
        return True
    if bounds is None:
        bounds = board_bounds(live_coords)
    print('--- steps left: ' + str(steps) + ' ---')
    print_board(live_coords, bounds)
    new_coords = step_forward(live_coords, bounds)
    simulate(new_coords, steps - 1, bounds)


def board_bounds(live_coords):
    """Given live coordinates, return the min x/y and max x/y."""
    if not live_coords:
        return False
    min_x = live_coords[0][0]
    max_x = live_coords[0][0]
    min_y = live_coords[0][1]
    max_y = live_coords[0][1]
    for i, j in live_coords:
        if min_x > i:
            min_x = i
        if i > max_x:
            max_x = i
        if min_y > j:
            min_y = j
        if j > max_y:
            max_y = j
    return [[min_x, min_y], [max_x, max_y]]


def print_board(live_coords, bounds=None):
    """Print out the board, live cells are *, dead ones are ."""
    if not live_coords:
        return False
    if bounds is None:
        bounds = board_bounds(live_coords)
    [[min_x, min_y], [max_x, max_y]] = bounds
    for i in range(min_x, max_x + 1):
        row = ''
        for j in range(min_y, max_y + 1):
            if [i, j] in live_coords:
                row += '*'
            else:
                row += '.'
        print(row)


def step_forward(live_coords, bounds=None):
    """Compute how each cell is affected."""
    if not live_coords:
        return False
    if bounds is None:
        bounds = board_bounds(live_coords)
    [[min_x, min_y], [max_x, max_y]] = bounds
    next_gen_live = []
    for i in range(min_x, max_x):
        for j in range(min_y, max_y):
            is_alive = [i, j] in live_coords
            if should_be_alive(live_coords, [i, j], is_alive):
                next_gen_live.append([i, j])
    return next_gen_live


def should_be_alive(live_coords=None, coord=None, is_alive=True):
    """
    Determine if a point is alive.

    Rules are:
     - Any live cell with less than two live neighbours dies.
     - Any live cell with two or three live neighbours remains living.
     - Any live cell with more than three live neighbours dies.
     - Any dead cell with exactly three live neighbours becomes a live cell.
     - A cell neighbours another cell if it is horizontally, vertically,
        or diagonally adjacent.
    """
    if not live_coords or not coord:
        return False
    num_alive = alive_neighbors(live_coords, coord)
    if is_alive:
        if num_alive < 2:
            return False
        elif num_alive == 2 or num_alive == 3:
            return True
        elif num_alive > 3:
            return False
    elif num_alive == 3:
        return True
    return False


def alive_neighbors(live_coords, coord):
    """Find out how many neighbors are alive (8 surrounding cells)."""
    if not live_coords or not coord:
        return False
    x, y = coord
    neighbors = [[(x - 1), y], [(x - 1), (y - 1)], [(x - 1), (y + 1)],
                 [(x + 1), y], [(x + 1), (y - 1)], [(x + 1), (y + 1)],
                 [x, (y - 1)], [x, (y + 1)]]
    intersection = [value for value in neighbors if value in live_coords]
    return len(intersection)


simulate([[0, 0], [0, 1], [1, 0], [3, 3], [3, 2], [2, 3]], steps=100)
