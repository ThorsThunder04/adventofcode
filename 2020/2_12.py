import re

testi = """1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc"""


def serialize(s: str) -> "list[tuple]": # output of form [((minOcc, maxOcc), char, password), ...]
    passwords = []
    lines = s.split("\n")
    for line in lines:
        omin, omax, char, pswd = re.match(r"(\d+)-(\d+) ([a-z]): (\w+)", line).groups()
        # I know I could check if they are valid right here, but I prefer have all the data first
        res = (int(omin), int(omax), char, pswd)
        passwords.append(res)
    
    return passwords

def nValidPasswords(data):

    nValid = 0

    for pswd in data:
        n, m, c, p = pswd

        if n <= p.count(c) <= m:
            nValid += 1
    
    return nValid

def nValidPasswords2(data):

    nValid = 0
    for pswd in data:
        n, m, c, p = pswd

        # using a XOR condition
        if (p[n-1] == c or p[m-1] == c) and not (p[m-1] == p[n-1] == c):
            nValid += 1
    
    return nValid

# part 1
print(nValidPasswords(serialize(testi)) == 2)
# print(nValidPasswords(serialize(open("2i.txt", "r").read())) == 655)

print(nValidPasswords2(serialize(testi)) == 1)
# print(nValidPasswords2(serialize(open("2i.txt", "r").read())) == 673)