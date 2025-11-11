
testi = """1721
979
366
299
675
1456"""


def serialize(s):
    return [int(num) for num in s.split("\n")]


def twoSum(targetSum: int, nums: list[int]) -> int:
    
    parsed = set()

    # while there isn't a complement to the current num[i], add num[i] to the list
    i = 0
    while (targetSum - nums[i]) not in parsed: 
        parsed.add(nums[i])
        i += 1
    
    return nums[i]*(targetSum-nums[i])

def threeSum(targetSum: int, nums: list[int]) -> int:
    # same approach as two sum, but we'll make a secondary sum for each number and then find a pair that sums to that
    tplt = None
    i = 0
    while i < len(nums) and tplt is None:

        secondSum = targetSum - nums[i]

        parsed = set()

        j = i
        while j < len(nums) and (secondSum - nums[j]) not in parsed:
            parsed.add(nums[j])
            j += 1

        if j < len(nums): # we didn't reach the end of the list => we found a solution
            tplt = (nums[i], nums[j], secondSum - nums[j])      
        
        i += 1
    
    return tplt[0]*tplt[1]*tplt[2]

# part 1
print(twoSum(2020, serialize(testi)) == 514579)
# print(twoSum(2020, serialize(open("1i.txt", "r").read())) == 786811)

#part 2
print(threeSum(2020, serialize(testi)) == 241861950)
# print(threeSum(2020, serialize(open("1i.txt", "r").read())) == 199068980)
