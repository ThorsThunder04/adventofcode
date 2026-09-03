import re

testi = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
testi2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"


def main(instr):

    matched = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", instr)

    res = [int(d1)*int(d2) for d1,d2 in matched]
    return sum(res)


def main2(instr):
    do = True
    s = 0
    matched = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", instr)
    for elt in matched:
        if elt == "do()": # if we hit a do(), set so that we continue multiplying after
            do = True
            continue
        elif elt == "don't()": # if we hit a don't(), set so that we skip all until we hit another do()
            do = False
            continue
        elif not do: # while we havn't hit another do()
            continue
        
        x,y = [int(x) for x in re.findall(r"\d{1,3}", elt)]
        s += x*y


    return s


print(main2(testi2))
# print(main2(open("3i.txt", "r").read()))