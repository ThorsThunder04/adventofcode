import math

testi = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""


def serialize(s):
    lines = s.split("\n")
    splitLines = [line.split(": ") for line in lines]
    return [(int(res), [int(num) for num in operands.split(" ")]) for res,operands in splitLines]


def allCombRes(nums, i):

    if i == len(nums)-1:
        return [nums[i]]
    else:
        retl = allCombRes(nums, i+1)
        currl = []
        for j in range(len(retl)):
            # print(nums[i], retl[j], retl)
            # part 2 = the last element in this list
            currl += [nums[i]+retl[j], nums[i]*retl[j], int(str(retl[j]) + str(nums[i]))]
        
        return currl


def main(data):


    calRes = 0
    for res, operands in data:
        all_results = allCombRes(operands[::-1], 0)
    
        # print(res, operands)
        # print(all_results, res in all_results)

        if res in all_results:
            # print(res)
            calRes += res
    
    return calRes

print(main(serialize(testi)))
# print(main(serialize(open("7i.txt", "r").read())))
    