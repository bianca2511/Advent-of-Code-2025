def parseInput(instruction):
    direction = instruction[0]
    distance = int(instruction[1:])
    return direction, distance

position = 50
code = 0
with open("input.txt") as f:
    for line in f:
        direction, distance = parseInput(line)
        if(direction == 'L'):
            position = (position-distance) % (100)
        elif(direction == 'R'):
            position = (position+distance) % (100)
            
        print(position)
        
        if position == 0:
            code += 1
        
print(code)