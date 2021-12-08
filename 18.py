triangle = [
    [75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20, 4, 82, 47, 65],
    [19, 1, 23, 75, 3, 34],
    [88, 2, 77, 73, 7, 63, 67],
    [99, 65, 4, 28, 6, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23],
]


def get_connected_losses(row, i, losses):
    if row == 0:
        return

    row_below = losses[row+1]
    return row_below[i:i+2]


def print_it(triangle, losses):
    current_pos = 0
    for i, row in enumerate(triangle):
        print(' ' * int(len(triangle) - i * 2 + 20), end='')
        for j, val in enumerate(triangle[i]):
            if j == current_pos:
                print(f'\033[92m{val:03d}\033[0m', end=' ')
            else:
                print(f'{val:03d}', end=' ')

        print(' ' * int(len(triangle) - i * 2 + 20) * 2, end='')
        for j, loss in enumerate(losses[i]):
            if j == current_pos:
                print(f'\033[93m{loss:03d}\033[0m', end=' ')
            else:
                print(f'{loss:03d}', end=' ')

        if i < len(triangle) - 1:
            options = losses[i+1][current_pos:min(current_pos+2, len(losses[i+1]))]

            if options[0] > options[1]:
                current_pos += 1

        print()



losses = []
for row in triangle:
    row_loss = []
    for n in row:
        row_loss.append(max(row) - n)

    losses.append(row_loss)

print('Original')
print_it(triangle, losses)

for row in range(len(triangle) - 2, -1, -1):
    for i, n in enumerate(losses[row]):
        connected_losses = get_connected_losses(row, i, losses)

        if not connected_losses:
            continue
        losses[row][i] += min(connected_losses)

print('Updated')
print_it(triangle, losses)
