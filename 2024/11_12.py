
from math import log10, floor

testi = "125 17"
fulli = "572556 22 0 528 4679021 1 10725 2790"


def serialize(s):
    nums = s.split(" ")
    return [int(d) for d in nums]

def dictAdd(d, key, val):
    if key in d:
        d[key] += val
    else: d[key] = val

def blinkStones2(sD):
    """
    This is basically just a highly optimized version of the part one algorithm I have
    Instead of keeping memory of every single number (even doubles), we keep memory of the frequency of each number instead.
    So each time we get to a number, we have that number and it's frequency. Then depending on what we need to do with that number,
    we just transfer the frequencies from that number to the new number(s)
    """


    # we need to use a new dictionary because since the previous one doesn't have order
    # we could end up parsing a number after it had been modified by a previous number we
    # just parced. It's just a tiny bit slow because of this
    newDict = {}


    i = len(sD)-1
    keys = list(sD.keys())
    while i >= 0:
        stone = keys[i]

        rep = sD[stone] # frequencies for that number
        if stone == 0:
            dictAdd(newDict, 1, rep)
        elif floor(log10(stone))%2 != 0:
            lg10 = (floor(log10(stone))+1)//2
            n1 = stone // (10**lg10)
            n2 = stone%(10**lg10)
            # we transfer the frequency to the first and second half
            dictAdd(newDict, n1, rep)
            dictAdd(newDict, n2, rep)
        else:
            dictAdd(newDict, stone*2024, rep)
            
        i -= 1
    
    return newDict


def nStones(stones, n):
    stonesDict = {}
    for stone in stones: # initialize dictionary with values
        dictAdd(stonesDict, stone, 1)

    for i in range(n):
        stonesDict = blinkStones2(stonesDict)

    return sum(stonesDict.values())

# print(nStones(serialize(testi, 75)))
print(nStones(serialize(fulli,75)))
