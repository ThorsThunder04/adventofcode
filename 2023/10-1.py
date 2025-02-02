"""
Concept:

Since the distance is measured by step for each tile we take and not by coordinate, we should count once in one direction and once in reverse.
This way when we eventually cross the same tile (determined by coordinate) for each direction, we can find out which was the maximum distance
that we recorded between each direction.

Or we can do one whole loop, and then eucludian division to go for half, and that would be the maximum distance. 
Since we will be travelling in a loop that repeats it's self. And eventually we will start approaching the start position again.

"""

example_input1 = """.....
.S-7.
.|.|.
.L-J.
....."""

example_input2 = """..F7.
.FJ|.
SJ.L7
|F--J
LJ..."""










def serialize_string(input_string):
    lines = input_string.split("\n")
    # we will also add margines to avoid index errors later
    list_lines = [["."] + list(line) ["."] for line in lines]
    list_lines = [["."]*len(list_lines[0])] + list_lines + [["."]*len(list_lines[0])]

    return list_lines



def follow_path_positions(pipe_map):
    moves = { # we hold the relative movements and the connection pipes
        "|": [(0, 1), ("|", "L", "J", "7", "F")], # these two depends on
        "-": [(1, 0), ("L", "J", "7", "F")], # the adjacent pipe leading to them
        "L": [(1,0),(["|", "7", "F"],["-", "J", "7"])], 
        "J": [(-1, 0),(["|", "7", "F"],["-", "L", "F"])],
        "7": [(-1, 0),(["-", "L", "F"],["|", "L", "J"])],
        "F": [(1, 0),(["-", "J", "7"],["|", "L", "J"])],
        "S": ()
    }

    # find the starting position
    first_pos = ()
    all_connected = True
    y = 1
    while y < len(pipe_map)-1:
        
        x = 1
        while not moves["S"] or x < len(pipe_map[0])-1:

            current_direction = pipe_map[y][x]
            rel_pos = {"L": pipe_map[y][x-1],
                            "R": pipe_map[y][x+1],
                            "U": pipe_map[y+1][x],
                            "D": pipe_map[y-1][x]}
            found_one = False

            if current_direction == "|":
                found_one = rel_pos["U"] in moves["|"][1] and rel_pos["D"] in moves["|"]
            elif current_direction == "-":
                found_one = rel_pos["R"] in moves["-"][1] and rel_pos["L"] in moves["-"]
            elif current_direction == "L":
                found_one = rel_pos["L"] in moves["L"][1][1] and rel_pos["U"] in moves["L"][1][0]
            elif current_direction == "J":
                found_one = rel_pos["U"] in moves["J"][1][0] and rel_pos["L"] in moves["J"][1][0]
            elif current_direction == ""
                
                
        # should maybe just model into a graph


        y += 1