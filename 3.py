maze = []

with open("data/3/input.txt") as input_file:
    for line in input_file.readlines():
        maze.append(line.strip())

height = len(maze)
width = len(maze[0])


def evaluate_slope(right_step, down_step):
    trees = 0
    pos = (0, 0)
    while pos[0] < height:
        new_pos = (pos[0] + down_step, (pos[1] + right_step) % width)
        if new_pos[0] >= height:
            break
        if maze[new_pos[0]][new_pos[1]] == '#':
            trees += 1
        pos = new_pos

    return trees


ans = evaluate_slope(1, 1) * evaluate_slope(3, 1) * evaluate_slope(5, 1) * evaluate_slope(7, 1) * evaluate_slope(1, 2)
print(ans)