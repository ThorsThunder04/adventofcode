from math import log10, floor

testi = "125 17"
fulli = "572556 22 0 528 4679021 1 10725 2790"


def serialize(s):
    nums = s.split(" ")
    return [int(d) for d in nums]


def blinkStones(stones: list[int]) -> list[int]:

    # newStones = []

    i = len(stones)-1
    while i >= 0:
        n = stones[i]
        if n == 0:
            # newStones.append(1)
            stones[i] = 1
        elif floor(log10(n))%2 != 0:
            lg10 = (floor(log10(n))+1)//2
            n1 = n // (10**lg10)
            n2 = n%(10**lg10)
            stones[i] = int(n2)
            # stones.insert(i, int(n1))
            # i += 1
            stones.append(n1)
        else:
            stones[i] *= 2024
        
        i -= 1
    return stones



def nStones(stones):

    for i in range(25):
        blinkStones(stones)
        # print(i)
        # print(stones)
    
    return len(stones)

print(nStones(serialize(testi)))
print(nStones(serialize(fulli)))
