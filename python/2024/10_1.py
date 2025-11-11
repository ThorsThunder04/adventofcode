
testi1 = """0123
1234
8765
9876"""

testi2 = """89010123
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

    

def searchTails(grid: list[list[int]], head: tuple[int,int], maxRows:int , maxColumns:int) -> int:
    """
    We find all tails by using a simple Breadth First Search
    """

    seen = set() # what nodes we have already visited
    tails = set() # what tails we have found
    toParse = [head]


    while len(toParse) > 0:
        currNode = toParse.pop(0)
        r,c = currNode

        if grid[r][c] == 9:
            tails.add(currNode)
        else:
            # get all adjacent nodes
            for rr,cc in surroundingNodes(currNode, maxRows, maxColumns):

                # if the next node is this one + 1 and it hasn't already been visited
                if grid[r][c] + 1 == grid[rr][cc] and (rr,cc) not in seen:
                    toParse.append((rr,cc))
        
        seen.add(currNode)
    
    return len(tails)

def searchAllHeads(grid):
    """
    Goes over every node and starts a search on all nodes with value 0
    Then sums all the results togehter
    """

    nHeads = 0
    maxRows = len(grid)
    maxColumns = len(grid[0])

    # there could maybe be a better way to find all the 0s
    for r in range(maxRows):
        for c in range(maxColumns):
            if grid[r][c] == 0:
                nHeads += searchTails(grid, (r,c), maxRows, maxColumns)
    
    return nHeads

print(searchAllHeads(serialize(testi1)) == 1)
print(searchAllHeads(serialize(testi2)) == 36)
# print(searchAllHeads(serialize(open("10i.txt", "r").read())))

