

testi = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

def serialize(instr):
    rules, updates = instr.split("\n\n")
    rules = [rule.split("|") for rule in rules.split("\n")]
    rules = [[int(a), int(b)] for a,b in rules]
    updates = [update.split(",") for update in updates.split("\n")]
    updates = [[int(x) for x in update] for update in updates]
    return rules, updates


def isWellOrderedI(update, i, rulesdict):
    if update[i] in rulesdict:
        return all([page not in update[:i] for page in rulesdict[update[i]]])
    return True



def main(data):

    rules, updates = data

    rulesdict = {}
    for rule in rules:
        x,y = rule
        if rulesdict.get(x) is None:
            rulesdict[x] = []
        
        rulesdict[x].append(y)

    rejupd = []
    for update in updates:
        valid = True
        i = 0
        while valid and i < len(update):
            if update[i] in rulesdict:
                valid = isWellOrderedI(update, i, rulesdict)
            i += 1
        
        if not valid:
            rejupd.append(update)
    

    for update in rejupd: # implementation of insertion sort :O
        i = len(update)-1
        while i > 0:
            j = i
            while update[i] in rulesdict and not isWellOrderedI(update, j, rulesdict):
                j -= 1

            if update[i] in rulesdict:
                update[j], update[i] = update[i], update[j]
            i -= 1
        # print(update)

    midvalues = 0
    for update in rejupd:
        midvalues += update[len(update)//2]

    return midvalues
    


print(main(serialize(testi)))
# print(main(serialize(open("5i.txt", "r").read())))

