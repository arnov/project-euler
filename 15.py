

def expand_path(point, grid_size):
    i, j = point

    outputs = []

    if i < grid_size:
        outputs.append((i+1, j))
    if j < grid_size:
        outputs.append((i, j+1))

    return outputs


def previous_points(point):
    i, j = point

    outputs = []

    if i > 0:
        outputs.append((i-1, j))
    if j > 0:
        outputs.append((i, j-1))

    return outputs


def main():
    grid_size = 20

    routes_to_point = {}

    for i in range(grid_size + 1):
        for j in range(grid_size + 1):
            routes_to_point[(i, j)] = 0

    routes_to_point[(0, 0)] = 1

    for point in sorted(routes_to_point):
        if point == (0, 0):
            continue

        for prev_point in previous_points(point):

            routes_to_point[point] += routes_to_point[prev_point]

    print(f'grid size: {grid_size}')
    print(f'routes to end: {routes_to_point[grid_size, grid_size]}')


if __name__ == '__main__':
    main()
