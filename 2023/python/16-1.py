example_input = open("16input.txt", "r").read()


def serialize_input(string):
    lines = string.split("\n")
    return [list(line) for line in lines]


def get_positions(grid_list, direction, start_coord=(0,0)):

    x,y = start_coord
    curr_char = grid_list[y][x]
    positions = [(x,y)]
    if x >= len(grid_list[0]) or x < 0 or y >= len(grid_list) or y < 0:
        return positions
    
    elif curr_char == "-":
        if direction in ("v", "^"):
            positions += get_positions(grid_list, ">", (x+1,y)) + get_positions(grid_list, "<", (x-1,y))

    elif curr_char == "|":
        if direction in (">", "<"):
            positions += get_positions(grid_list, "v", (x, y+1)) + get_positions(grid_list, "^", (x,y-1))

    elif curr_char == "/":
        if direction == ">":
            positions += get_positions(grid_list, "^", (x,y-1))
        elif direction == "<":
            positions += get_positions(grid_list, "v", (x,y+1))
        elif direction == "^":
            positions += get_positions(grid_list, ">", (x+1, y))
        elif direction == "v":
            positions += get_positions(grid_list, "<", (x-1, y))
    elif curr_char == "\\":
        if direction == ">":
            positions += get_positions(grid_list, "v", (x,y+1))
        elif direction == "<":
            positions += get_positions(grid_list, "^", (x,y-1))
        elif direction == "^":
            positions += get_positions(grid_list, "<", (x-1, y))
        elif direction == "v":
            positions += get_positions(grid_list, ">", (x+1, y))
    else:
        if direction == ">":
            x += 1
        elif direction == "<":
            x -= 1
        elif direction == "v":
            y += 1
        elif direction == "^":
            y -= 1
        positions += get_positions(grid_list, direction, (x,y))
    return positions

serialized_input = serialize_input(example_input)
positions = get_positions(serialized_input, ">", (0,0))

for i in range(len(serialized_input)):
    for j in range(len(serialized_input[i])):
        if (j,i) in positions or serialized_input[i][j] != ".":
            serialized_input[i][j] = "#"

print("\n".join(["".join(line) for line in serialized_input]))


    