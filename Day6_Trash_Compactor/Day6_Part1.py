with open("input.txt") as f:
    lines = f.read().splitlines()

numbers = []
for elem in lines[:len(lines)-1]:
    row = list(map(int,elem.split()))
    numbers.append(row)
     
operations = lines[-1].split()

print(numbers)
print(operations)

countEquations = len(numbers[0])
grandTotal = 0

for i in range(countEquations):
    operation = operations[i]
    if operation == "+":
        equationResult = 0
        for row in numbers:
            equationResult += row[i]
    else:
        equationResult = 1
        for row in numbers:
            equationResult *= row[i]
    print(equationResult)
    grandTotal += equationResult
    
print(grandTotal)