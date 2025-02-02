
testi = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""


def isCross(instr, y,x):

    relpos = [
        [(i,i) for i in  range(3)], # diag down right
        # [(-i,i) for i in  range(4)], # diag up right
        [(i,-i) for i in range(3)], # diag down left
        # [(-i,-i) for i in range(4)] # diag up left
    ]

    counter = 0
    if x < len(instr[0])-2:
        word1 = "".join([instr[y+i][x+j] for i,j in relpos[0]])
        if word1 in ("MAS", "SAM"): counter += 1

        word2 = "".join([instr[y+i][x+j+2] for i,j in relpos[1]])
        if word2 in ("MAS", "SAM"): counter += 1
        if counter == 2:
            print(word1, word2)
     
    
    
    return counter == 2


def main(instr):
    instr = instr.split("\n")

    counter = 0
    for i in range(0, len(instr)-2):
        for j in range(0, len(instr)):
            if isCross(instr, i,j): counter += 1

    return counter

print(main(testi))
# print(main(open("4i.txt", "r").read()))
