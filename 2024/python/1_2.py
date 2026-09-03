
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
    l1, l2 = [list(l) for l in list(zip(*data))]

    simScore = 0
    while len(l1) > 0:
        num = l1.pop()
        occ1 = 1 # how many times num is in l1
        occ2 = 0 # how many times num is in l2
        i = 0
        while len(l1) > 0 and i < len(l1): # each time we remove the num from the list and increment the number of occurences of the number
            if l1[i] == num: 
                l1.pop(i)
                occ1 += 1
            else:
                i += 1

        i = 0
        # we count the number of occurences of the number in the other list
        while len(l2) > 0 and i < len(l2):
            if l2[i] == num:
                l2.pop(i)
                occ2 += 1
            else:
                i += 1
        
        simScore += (num*occ2)*occ1
    
    return simScore

print(main(testi))
# print(main(open("1i.txt", "r").read()))
        

    