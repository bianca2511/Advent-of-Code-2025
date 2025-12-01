def parseInput(instruction):
    direction = instruction[0]
    distance = int(instruction[1:])
    return direction, distance


position = 50
code = 0
zeroPasses = 0
with open("input.txt") as f:
    for line in f:
        direction, distance = parseInput(line)
        # flip to allow easier calculation of zero passes
        # use the same forumla as for a Right rotation
        if(direction == 'L'):
            flipped_position = (100-position)%100 
            zeroPasses += (flipped_position + distance)//100
            position = (position-distance) % (100)
            
        elif(direction == 'R'):
            zeroPasses += (position + distance) // 100
            position = (position+distance) % (100)
                
print(zeroPasses)
