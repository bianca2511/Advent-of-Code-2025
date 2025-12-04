with open("input.txt") as f:
    paperMap = f.read().splitlines()

# pad map with spaces around the edge rolls to make it easier to check neighbors 
def padMap(paperMap):
    paperMap = ['.' + row + '.' for row in paperMap]
    width = len(paperMap[0])
    emptySpace = '.' * width
    paperMap.insert(0, emptySpace)
    paperMap.append(emptySpace)

    return paperMap

paperMap = padMap(paperMap)

width_end = len(paperMap[0]) - 1
length_end = len(paperMap) - 1
countAccessibleRolls = 1 #just to make sure the first iteration happens
removableRolls = []
removed = []

# while there are still accessible rolls, repeat the process
while countAccessibleRolls > 0:
    countAccessibleRolls = 0 # reset the count
    
    for i in range(1, width_end):
        for j in range(1, length_end):
            if paperMap[i][j] == '@': # if we find roll
                neighbors = [paperMap[i-1][j-1] == '@', paperMap[i-1][j] == '@', paperMap[i-1][j+1] == '@', paperMap[i]
                            [j-1] == '@', paperMap[i][j+1] == '@', paperMap[i+1][j-1] == '@', paperMap[i+1][j] == '@', paperMap[i+1][j+1] == '@']
                count = sum(neighbor == True for neighbor in neighbors) # check neighbor paper rolliness count 
                if count < 4: # if less than 4 rolls around, it is accessible
                    countAccessibleRolls += 1
                    removableRolls.append([i,j]) # store position so we can remove it later
                    # removing here would mess up the next rolls neighbor calculation in this iteration
    removed.append(countAccessibleRolls) # save how many rolls were removed in this iteration
    
    # mark removed rolls with x
    for position in removableRolls:
            newRow = ''
            # paperMap[position[0]][position[1]] = 'x' #strings are immutable in Python so this doesnt work
            # need to make a new string
            # could have been avoided if i expanded the string into list of chars, but it's ok, learned something new
            newRow = paperMap[position[0]][:position[1]] + 'x' + paperMap[position[0]][position[1]+1:]
            paperMap[position[0]] = newRow
            
print(removed)
print(sum(removed))