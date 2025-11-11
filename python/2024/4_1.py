
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


def countxmaxfrompos(instr, y,x):

    relpos = [
        [(i,i) for i in  range(4)], # diag down right
        # [(-i,i) for i in  range(4)], # diag up right
        [(i,-i) for i in range(4)], # diag down left
        # [(-i,-i) for i in range(4)] # diag up left
    ]

    counter = 0
    if x < len(instr[0])-3:
        word = "".join([instr[y+i][x+j] for i,j in relpos[0]])
        if word in ("XMAS", "SAMX"): counter += 1
    
    if x >= 3:
        word = "".join([instr[y+i][x+j] for i,j in relpos[1]])
        if word in ("XMAS", "SAMX"): counter += 1
    
    return counter


def main(instr):

    counter = 0
    counter += instr.count("XMAS")
    counter += instr.count("SAMX")
    instr = instr.split("\n")
    transposedinstr = ""
    for i in range(len(instr[0])):
        for j in range(len(instr)):
            transposedinstr += instr[j][i]
    
    counter += transposedinstr.count("XMAS")
    counter += transposedinstr.count("SAMX")
    
    for i in range(0, len(instr)-3):
        for j in range(0, len(instr)):
            counter += countxmaxfrompos(instr, i, j)

    return counter

print(main(testi))
# print(main(open("4i.txt", "r").read()))
