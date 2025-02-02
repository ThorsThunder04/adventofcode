import re

testi = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""


def serialize(s):
    lines = s.split("\n")
    return [list(line) for line in lines]

def isNode(c):
    return re.match(r"[A-Z0-9]", c, re.IGNORECASE) is not None

def pointDiff(pt1, pt2): 
    # gets difference between x and y of two points
    x1,y1 = pt1
    x2,y2 = pt2
    return abs(x1-x2), abs(y1-y2)

def findAllOcc(grid, startRow, nodeFreq, startpt):
    # find all positions of nodes of the frequency nodeFreq
    coords = []
    for r in range(startRow, len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == nodeFreq and (r,c) != startpt:
                coords.append((r,c))
    
    return coords

def main(grid):

    nAntiNodes = set()

    gRowMax = len(grid)
    gColMax = len(grid[0])

    for r in range(gRowMax):
        for c in range(gColMax):

            if isNode(grid[r][c]): # if on a node
                freq = grid[r][c]
                otherNodes = findAllOcc(grid, r, freq, (r,c))

                for rr,cc in otherNodes:
                    rd,cd = pointDiff((r,c), (rr,cc))

                    offset = -1 if cc < c else 1 # useful for getting both anti nodes on both sides of the symmetry axis
                    # if the anti nodes are in bounds, add them to the list
                    if 0 <= rr + rd < gRowMax and 0 <= cc + cd*offset < gColMax: # downward axis
                        nAntiNodes.add((rr+rd, cc + cd*offset))
                    if 0 <= r - rd < gRowMax and 0 <= c - cd*offset < gColMax: # upward axis
                        nAntiNodes.add((r-rd, c-cd*offset))
    
    return len(nAntiNodes)


print(main(serialize(testi)))
# print(main(serialize(open("8i.txt", "r").read())))


    

