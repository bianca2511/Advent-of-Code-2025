with open("input.txt") as f:
    lines = f.read()
    lines = lines.split(",")

def parseRange(range):
    range_array = range.split("-")
    start = int(range_array[0])
    end = int(range_array[1])
    return start, end

def calculateNoDigits(number):
    numberDigits = 0
    while number:
        numberDigits += 1
        number //= 10
    return numberDigits
result = []
for line in lines:
    start, end = parseRange(line)
    for i in range(start, end):
        if calculateNoDigits(i) % 2 == 0:
            half = calculateNoDigits(i) // 2
            number_array = list(str(i))
            invalid = True
            for j in range(half):
                if number_array[j] != number_array[j+half]:
                    invalid = False
            if invalid == True:
                result.append(i)
# print(result)
print(sum(result))
    
