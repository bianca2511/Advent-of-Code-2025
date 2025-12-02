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


def findDivisors(number):
    divisors = [1]
    for d in range(2, number):
        if number % d == 0:
            divisors.append(d)
    return divisors


def checkDuplicate(number, list):
    for elem in list:
        if elem == number:
            return True
    return False

# Find number of divisors of digit count (to see how many repeating group sare possible)
# Only check for those configurations
# Divide by 10**d and check the last d digit group is always the same


result = []
for line in lines:
    start, end = parseRange(line)
    for i in range(start, end+1):
        if i < 10:  # patterns must repeat at least twice, so 1 digit numbers are valid
            continue
        digitCount = calculateNoDigits(i)
        divisors = findDivisors(digitCount)
        # print(f"{i} digits means {divisors} groups")
        for divisor in divisors:
            invalid = True
            divideBy = 10 ** divisor
            oldGroup = i % divideBy
            aux = i  # auxiliary var so i is not destroyed
            # check if the new group matches the old group
            while aux:
                group = aux % divideBy
                if group != oldGroup:  # if mismatch, break the loop
                    invalid = False
                    break
                oldGroup = group
                aux = aux // divideBy
            if invalid == True and checkDuplicate(i, result) == False:
                # for 555555, it can be 55-55-55 or 555-555 but it should only be added once
                # so we check it is already exists in the result array
                result.append(i)


print(result)
print(sum(result))
