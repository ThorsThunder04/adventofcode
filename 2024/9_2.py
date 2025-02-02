

testi = "2333133121414131402"


def createFileBlocks(s):

    outstr = ""
    isFile = True
    fileId = 0
    for c in s:
        d = int(c)
        if isFile:
            outstr += (str(fileId)+"-")*d
            fileId += 1
        else:
            outstr += ".-"*d
        isFile = not isFile
    return outstr

def newDataStruct(data):
    """
    returns a list of tuples of the form (string, nReptitions)
    so each tuple contains a string and how many times that string is present in a row in that position
    """
    
    data = data.strip("-").split("-")
    struct = []
    
    i = 0
    while i < len(data): # for each string
        currNum = data[i]
        n = 0
        j = i
        while j < len(data) and data[j] == currNum: # while we are on the same string
            n += 1
            j += 1
        struct.append((currNum, n))
        i = j
    
    return struct

def moveBlocks2(data):
    data = newDataStruct(data)
    # starti = 0
    endi = len(data)-1
    while data[endi][0] == ".": endi -= 1

    while endi > 0: # while we haven't parsed the whole list

        i = 0
        while i < endi: # from 0 to the current number we are treating
            if data[i][0] == "." and data[i][1] >= data[endi][1] and data[endi][0] != ".":
                d1, n1 = data[i]
                d2, n2 = data[endi]
                if (n1 - n2) == 0: # if it is a perfect fit, we just permutate the two strings
                    data[i], data[endi] = data[endi], data[i]
                else: # otherwise we calculate the difference
                    data[i] = (d1, n1-n2) # update the "." tuple after insertion of the file
                    data.insert(i, (d2,n2)) # insert the file
                    endi += 1 # because there is a new element in the list (at index i)
                    data[endi] = (d1,n2) # update where the file was and add empty space of the same size as the file
                
                i = endi # just to stop the loop
            else: 
                i+=1
        endi -= 1
        # print(endi)
                
    return data

def checkSum2(data):

    # make a list that contains each string individually | [("hi", 3)] => ["hi", "hi", "hi"]
    flattened = []
    for c,n in data:
       flattened += [c]*n
    
    # do the check sum, and skip dots
    s = 0
    for i in range(len(flattened)):
        if flattened[i] != ".":
            d = int(flattened[i])
            s += i*d
    return s

def checkSum3(data):
    s = 0
    j = i = 0
    while j < len(data):

        k = data[j][1] + i
        if data[j][0] != '.':
            d = int(data[j][0])
            
            # doing sum of i to k
            # s += d*(k*(k-1)//2 - i*(i-1)//2)
            s += d*((k**2 - k - i**2 + i)//2)

        i = k
        j += 1
    return s
            


print(checkSum3(moveBlocks2(createFileBlocks(testi))))
# print(checkSum3(moveBlocks2(createFileBlocks(open("9i.txt", "r").read()))) == 6418529470362)