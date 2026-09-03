import hashlib as hl

def tomd5(x):
    return hl.md5(str(x).encode("utf")).hexdigest()

def isAdventCoin(string):
    md5 = tomd5(string)
    return all([md5[i] == "0" for i in range(6)])

def findAdventCoin(string):

    n = 1

    while not isAdventCoin(string+str(n)):
        # print(n)
        n += 1
    return n

print(findAdventCoin("bgvyzdsv"))