
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
# brute force by checking every position the guard goes over
# for each position, add an obstruction
# if there is a loop, then the guard goes over one position twice while going in the same direction. 
# we check if there is two position with the same direction of the visited positions

def serialize(instr):
    grid = [list(line) for line in instr.split("\n")]
    startingPos = [] 
    for i in range(len(grid)):
        if "^" in grid[i]:
            startingPos = [i, grid[i].index("^")]
    
    return grid, startingPos

def getDirection(i):

    vd,hd = [(-1,0), (0,1), (1,0), (0,-1)][i]
    
    return vd, hd

def getVisitedTiles(startingPos, grid):

    # 0: up, 1: right, 2: down, 3: left
    d = 0
    # vertical direction, horizontal direction
    vd, hd = getDirection(d)
    r,c = startingPos
    positionsVisited = set()

    # if the next position is in bounds
    while 0 <= r+vd < len(grid) and 0 <= c+hd < len(grid[0]):

        pos = (r,c)
        positionsVisited.add(pos) # log the current position

        # if the next position is an obstacle, change direction
        if grid[r+vd][c+hd] == "#":
            d = (d+1)%4
            vd,hd = getDirection(d)
        else:
            r += vd
            c += hd
    

    # we always check for the next position, so we don't end up logging the last position
    positionsVisited.add((r,c))

    return list(positionsVisited)

def movePos(r,c,vd,hd):
    return r+vd, c+hd

def hasLoop(grid, startingPos, obstacle):
    """
    We parse the grid as usual like part 1 but we also add an obstacle.
    In addition, we log the visited positions with not only the coordinates, but also the direction.
    If we end up going over the same position in the same direction twice, then we are going in a loop.
    """

    r,c = startingPos

    # 0: up, 1: right, 2: down, 3: left
    d = 0

    # current direction
    vd,hd = getDirection(d)

    visited_tiles = set()

    # if we haven't been here in this direction before, and the next position is in bounds
    while (r,c,d) not in visited_tiles and (0 <= r+vd < len(grid)) and (0 <= c+hd < len(grid[0])):


        visited_tiles.add((r,c,d))
        # if the next position is and obstacle
        if grid[r+vd][c+hd] == "#" or (r+vd,c+hd) == obstacle:
            d = (d+1)%4
            vd,hd = getDirection(d)
        else: # otherwise move forward
            r += vd
            c += hd

    
    return (r,c,d) in visited_tiles

    

def main(data):
    grid, startingPos = data

    visited_positions = getVisitedTiles(startingPos, grid)
    print("Part 1:", len(visited_positions))
    nLoops = 0
    for x,y in visited_positions:
        # print(i)
        # if x != startingPos[0] and y != startingPos[1]:
        l = hasLoop(grid, startingPos, (x,y))
        if l:
            nLoops += 1
    
    return nLoops
        


print("Part 2:", main(serialize(testi)))
# print("Part 2:", main(serialize(open("6i.txt", "r").read())))
    
