with open("input.txt") as f:
    lines = f.read().splitlines()

numbers = []
countRows = 0

for elem in lines[:len(lines) - 1]:
    row = []
    for char in elem:
        if char == " ":
            row.append(0)  # Preserve spaces
        else:
            row.append(int(char))  # Convert digits to integers
    numbers.append(row)
    countRows +=1

operations = lines[-1].split()

    
print(countRows)
print(numbers)
print(operations)

countEquations = len(numbers[0])
grandTotal = 0
finalNumbers = []

# Merge the numbers by reading them in the cephalopode way
for i in range(countEquations):
    mergedNumber = 0
    for row in numbers:
        mergedNumber = mergedNumber * 10 + row[i]
    while mergedNumber > 0 and mergedNumber % 10 == 0:
        mergedNumber = mergedNumber // 10
    finalNumbers.append(mergedNumber)
print(finalNumbers)

sublists = []
currentSublist = []

for number in finalNumbers:
    if number == 0:
        sublists.append(currentSublist)
        currentSublist = []
    else:
        currentSublist.append(number)
        
if currentSublist:
    sublists.append(currentSublist)
print(sublists)


for i in range(len(sublists)):
    operation = operations[i]
    if operation == "+":
        equationResult = 0
        for number in sublists[i]:
            equationResult += number
    else:
        equationResult = 1
        for number in sublists[i]:
            equationResult *= number
    grandTotal += equationResult
    
print(grandTotal)