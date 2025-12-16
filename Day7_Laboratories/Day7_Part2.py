with open("input.txt") as f:
    lines = f.read().splitlines()

# Turn strings into list for easier assignment of new values
for index, line in enumerate(lines):
    lines[index] = list(line)

# Initial split location
splitterLocations = [lines[0].index('S')]

# Helper method to print the matrix
def printLines(lines):
    for line in lines:
        print(''.join(map(str, line)))
    print('\n')

printLines(lines)
n = len(lines)

# Initialize the timelines grid
rows, cols = n, len(lines[0])
timelines = [[0] * cols for _ in range(rows)]
timelines[0][splitterLocations[0]] = 1  # Start with 1 timeline at 'S'

printLines(timelines)

for index in range(1, n):
    for splitter in range(cols):
        if lines[index][splitter] == '.':
            # Add timelines from the cell directly above
            timelines[index][splitter] += timelines[index-1][splitter]
        elif lines[index][splitter] == '^':
            # Split timelines to the left and right
            if splitter > 0 and lines[index][splitter-1] == '.':
                timelines[index][splitter-1] += timelines[index-1][splitter]
            if splitter < cols - 1 and lines[index][splitter+1] == '.':
                timelines[index][splitter+1] += timelines[index-1][splitter]

printLines(timelines)

# Sum up the timelines in the last row
totalTimelines = sum(timelines[-1])
print("Count timelines: ", totalTimelines)