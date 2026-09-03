"""
This part is also present in part 2, thus the 6_12 (part 1 and 2)
And the version in part 2 seems less messy. Just and FYI
"""


testi = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""


def serialize(instr):
    grid = [list(line) for line in instr.split("\n")]
    startingPos = [] 
    for i in range(len(grid)):
        if "^" in grid[i]:
            startingPos = [i, grid[i].index("^")]
    
    return grid, startingPos


def main(data):
    grid, startingPos = data


    vd = -1
    hd = 0
    r,c = startingPos
    positionsVisisted = []
    while 0 <= r+vd < len(grid) and 0 <= c+hd < len(grid[0]):

        positionsVisisted.append((r,c)) # log the current position

        dire = (vd,hd)
        # print(r,c)
        if dire == (-1,0): # if going up
            if grid[r+vd][c+hd] == "#":
                vd = 0
                hd = 1
        elif dire == (1,0): # if going down
            if grid[r+vd][c+hd] == "#":
                vd = 0
                hd = -1
        elif dire == (0, -1): # if going left
            if grid[r+vd][c+hd] == "#":
                vd = -1
                hd = 0
        elif dire == (0,1): # if going right
            if grid[r+vd][c+hd] == "#":
                vd = 1
                hd = 0

        r += vd
        c += hd
        # print(positionsVisisted)

    positionsVisisted.append((r,c))

    return len(set(positionsVisisted))
            

print(main(serialize(testi)))
# print(main(serialize(open("6i.txt", "r").read())))
    
