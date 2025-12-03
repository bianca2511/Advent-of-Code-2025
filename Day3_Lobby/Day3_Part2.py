# find the leftmost highest digit leaving at least 11 left
# find leftmost highest digit leaving at least 10left

with open("input.txt") as f:
    lines = f.read().splitlines()

result = []
for bank in lines:
    bank = list(bank)
    bank = list(map(int, bank))
    bankLength = len(bank)
    countBatteries = 12
    batteryIndex = -1
    max_element = 0
    bankResult = []
    
    # print(f"BATTERY BANK {bank}")
    while countBatteries > 0:
        max_element = 0
        start = batteryIndex + 1
        end = bankLength - countBatteries
        for i in range(start, end+1):
            # print(f"index {i}, element {bank[i]}")
            if bank[i] > max_element:
                max_element = bank[i]
                batteryIndex = i
        bankResult.append(max_element)
        countBatteries -=1
        # print(f"max: {max_element}, battery index {batteryIndex}")

    bankResult = list(map(str, bankResult))
    bankResult = "".join(bankResult)
    result.append(bankResult)

result = list(map(int,result))
print(result)
print(sum(result))   
