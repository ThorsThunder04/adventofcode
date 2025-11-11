example_input = """2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533"""


def serialize_input(string):
    lines = string.split("\n")
    lines = [list(line) for line in lines]
    return lines


def find_best_path(input_data):
    
    moves = []
    relative_moves = {
        "<": [(-1,0), (0,1), (0,-1)],
        ">": [(1,0), (0,1), (0,-1)],
        "v": [(0,-1), (1,0), (-1,0)],
        "^": [(0, 1), (1, 0), (-1, 0)]
    }

    

