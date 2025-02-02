
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

    accepted_updates = []
    for update in updates:
        valid = True
        for i in range(len(update)):
            if update[i] in rulesdict:
                valid = valid and isWellOrderedI(update, i, rulesdict)
        
        if valid:
            accepted_updates.append(update)
    
    midvalues = 0
    for update in accepted_updates:
        midvalues += update[len(update)//2]

    return midvalues
    


print(main(serialize(testi)))
# print(main(serialize(open("5i.txt", "r").read())))

