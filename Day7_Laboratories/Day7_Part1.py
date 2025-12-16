with open("input.txt") as f:
    lines = f.read().splitlines()
    
print(lines)

splitterLocations = [lines[0].find('S')]
countSplits = 0

def printLines(lines):
    for line in lines:
        print(line)
        
n = len(lines)
for index in range(1, n):
    newSplitterLocations = []
    for splitter in splitterLocations:
        # printLines(lines)
        if lines[index][splitter] == '.':
            lines[index] = lines[index][:splitter] + '|' + lines[index][splitter+1:]
            newSplitterLocations.append(splitter)
        elif lines[index][splitter] == '^':
            countSplits +=1
            if splitter > 0  and lines[index][splitter-1] != '|':
                lines[index] = lines[index][:splitter-1] + '|' + lines[index][splitter:]
                newSplitterLocations.append(splitter-1)
            if splitter < n - 1 and lines[index][splitter+1] != '|':
                lines[index] = lines[index][:splitter+1] + '|' + lines[index][splitter+2:]
                newSplitterLocations.append(splitter+1)
    splitterLocations = newSplitterLocations
    # print("new splitter locations: ", newSplitterLocations)

printLines(lines)
print("Count splits: ", countSplits)