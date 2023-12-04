from collections import defaultdict

p1 = 0
p2 = defaultdict(int)
with open('./Day4/list.txt') as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        p2[i] += 1
        first, rest = line.split('|')
        id_, card = first.split(':')
        card_nums = [int(x) for x in card.split()]
        rest_nums = [int(x) for x in rest.split()]
        val = len(set(card_nums) & set(rest_nums))
        if val > 0:
            p1 += 2**(val-1)
        for j in range(val):
            p2[i+1+j] += p2[i]
        
    print("Part1: ", p1)
    print("Part2: ", sum(p2.values()))