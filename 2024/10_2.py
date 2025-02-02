
testi = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""


def serialize(s: str) -> list[list[int]]:
    linesSplit = [list(line) for line in s.split("\n")]
    linesInt = [[int(d) for d in line] for line in linesSplit]
    return linesInt

def surroundingNodes(pos, maxRows, maxColumns):

    r,c = pos
    offsets = [(-1,0), (1,0), (0,1), (0,-1)]
    adjPos = []

    for ro,co in offsets:
        if 0 <= r+ro < maxRows and 0 <= c+co < maxColumns:
            adjPos.append((r+ro,c+co))
    
    return adjPos

    

def searchPathRatings(grid: list[list[int]], head: tuple[int,int], maxRows:int , maxColumns:int) -> int:
    """
    Still while using a Breadth First Search. But it's modified, given the properties of the input graph (`grid`)

    Since all adjacent nodes to the current one are it's value + 1
    We can conclude that the graph `grid` is acyclic, and so there are no infinite loops.
    This allows us to remove the seen set, as a given path will either lead up to 9 or stop (no more adjacent nodes)
    (this is in comparison to 10_1.py)
    """

    rating = 0
    toParse = [head]

    while len(toParse) > 0:
        currNode = toParse.pop(0)
        r,c = currNode

        # each time we reach a 9 we have found a new path, so we increment the rating by 1.
        if grid[r][c] == 9:
            rating += 1
        else:
            # get all adjacent nodes
            for rr,cc in surroundingNodes(currNode, maxRows, maxColumns):

                if grid[r][c] + 1 == grid[rr][cc]:
                    toParse.append((rr,cc))
        
            # seen.add(currNode)
    
    return rating

def searchAllHeads(grid):
    """
    Goes over every node and starts a search on all nodes with value 0
    Then sums all the results togehter
    """
    allRatings = 0
    maxRows = len(grid)
    maxColumns = len(grid[0])

    # there could maybe be a better way to find all the 0s
    for r in range(maxRows):
        for c in range(maxColumns):
            if grid[r][c] == 0:
                allRatings += searchPathRatings(grid, (r,c), maxRows, maxColumns)
    
    return allRatings

print(searchAllHeads(serialize(testi)) == 81)
# print(searchAllHeads(serialize(open("10i.txt", "r").read())) == 1326)

