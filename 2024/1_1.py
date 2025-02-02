
testi = """3   4
4   3
2   5
1   3
3   9
3   3"""

def serializeStr(string):
    splitLines = string.split("\n")
    splitLPairs = [line.split("   ") for line in splitLines] 
    return [(int(d1), int(d2)) for d1,d2 in splitLPairs]


def main(inStr):
    data = serializeStr(inStr)
    l1, l2 = [list(l) for l in list(zip(*data))] # puts each column in individual lists

    diffs = []
    while len(l1) > 0 and len(l2) > 0: # calculate all the differences between the minimum values
        # gets the minimum value from each list, and removes them from the list at the same time
        m1 = l1.pop(l1.index(min(l1)))
        m2 = l2.pop(l2.index(min(l2)))
        diffs.append(abs(m1 - m2))
    
    return sum(diffs)

print(main(testi))
# print(main(open("1i.txt", "r").read()))
        

    