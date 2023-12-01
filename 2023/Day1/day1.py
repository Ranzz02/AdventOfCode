import json
f = open("./list.json")
p1 = 0
p2 = 0
for line in json.load(f):
    p1list = []
    p2list = []
    for index, char in enumerate(line):
        if char.isdigit():
            p1list.append(char)
            p2list.append(char)
        for d, val in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
            if line[index:].startswith(val):
                p2list.append(str(d+1))
    p1 += int(p1list[0]+p1list[-1])
    p2 += int(p2list[0]+p2list[-1])
print("Final output p1: ", p1, "/ Final output p2: ", p2)
f.close()