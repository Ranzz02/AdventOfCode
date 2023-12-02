import re
with open("./2023/Day2/list.txt") as f:
    red = 12
    green = 13
    blue = 14

    valid = True
    output_1 = 0
    output_2 = 0
    for line in f.readlines():
        data = line.split(':')
        index = data[0].split(' ')[1]
        valid = True
        power = 0
        
        min_red = 0
        min_green = 0
        min_blue = 0

        for game in data[1].split(r';'):
            for cube in game.split(r','):
                cube = cube.split(r' ')
                val = cube[1]
                color = cube[2].strip('\n')
                if color == 'red':
                    if int(val) > red:
                        valid = False

                    if int(val) > min_red:
                        min_red = int(val)
                elif color == 'green':
                    if int(val) > green:
                        valid = False
                        
                    if int(val) > min_green:
                        min_green = int(val)
                elif color == 'blue':
                    if int(val) > blue:
                        valid = False
                        
                    if int(val) > min_blue:
                        min_blue = int(val)

        power += min_red * min_green * min_blue
        if valid:
            output_1 += int(index)

        output_2 += power
    
    print("Final output: ", output_1, " Part two: ", output_2)