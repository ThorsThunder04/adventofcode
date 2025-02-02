
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


def moveBlocks(data: str):

    data = data.strip("-").split("-")
    
    # print(newDataStruct(data))
    lasti = len(data)-1
    while data[lasti] == ".":
        lasti -= 1

    firsti = data.index(".")

    while lasti > firsti:

        if data[firsti] == "." and data[lasti] != ".":
            data[firsti], data[lasti] = data[lasti], data[firsti]
            # firsti += 1
            # lasti -= 1
        if data[firsti] != ".":
            firsti += 1
        if data[lasti] == ".":
            lasti -= 1
    
    # print("-".join(data))
    return data


def checkSum(data):
    s = 0
    i = 0
    while data[i] != ".":
        d = int(data[i])
        s += i*d
        i+=1
    return s


print(checkSum(moveBlocks(createFileBlocks(testi))))
# print(checkSum(moveBlocks(createFileBlocks(open("9i.txt", "r").read()))))
