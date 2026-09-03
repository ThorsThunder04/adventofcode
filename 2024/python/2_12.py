
testi = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""


def serialize(string):
    return [[int(num) for num in line.split(" ")] for line in string.split("\n")]

def isLineSafe(line):
    safe = True
    # check if all decreasing or increasing
    safe = safe and (all([line[i-1] > line[i] for i in range(1, len(line))]) 
                     or all([line[i-1] < line[i] for i in range(1, len(line))]))

    # check if all the differences are withing the accepted amount
    i = 1
    while safe and i < len(line):
        diff = abs(line[i-1] - line[i])
        if not (1 <= diff <= 3): safe = False
        i+=1
    
    return safe


def isLineSafeBis(line):
    # not the most efficient way of doing this
    if isLineSafe(line): return True
    else: # if not already safe
        # check if by removing one level, the report becomes safe
        i = 0
        while i < len(line):
            if isLineSafe(line[:i] + line[i+1:]):
                return True
            i+=1

    
    return False


def howManySafe(inStr):
    data = serialize(inStr)
    counter = 0
    for line in data:
        if isLineSafeBis(line): 
            print(line)
            counter += 1
    
    return counter

print(howManySafe(testi))
# print(howManySafe(open("2i.txt", "r").read()))
