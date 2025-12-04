with open("input.txt") as f:
    paperMap = f.read().splitlines()


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
countAccessibleRolls = 0

for i in range(1, width_end):
    for j in range(1, length_end):
        if paperMap[i][j] == '@':
            neighbors = [paperMap[i-1][j-1] == '@', paperMap[i-1][j] == '@', paperMap[i-1][j+1] == '@', paperMap[i]
                        [j-1] == '@', paperMap[i][j+1] == '@', paperMap[i+1][j-1] == '@', paperMap[i+1][j] == '@', paperMap[i+1][j+1] == '@']
            count = sum(neighbor == True for neighbor in neighbors)
            print(f"neighbors: {neighbors}, count:{count}")
            if count < 4:
                countAccessibleRolls += 1
print(countAccessibleRolls)