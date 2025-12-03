with open("input.txt") as f:
    lines = f.read().splitlines()


result = []
for bank in lines:
    bank = list(bank)
    bank = list(map(int, bank))
    n = len(bank)
    
    max_first_battery = 0
    max_first_index = 0
    max_second_battery = 0
    
    for i in range(n-1):
        if bank[i] > max_first_battery:
            max_first_battery = bank[i]
            max_first_index = i
    

    for j in range(n-1, max_first_index, -1):
        if bank[j] > max_second_battery:
            max_second_battery = bank[j]
    
    result.append(int(str(max_first_battery)+str(max_second_battery)))
    
print(result)
print(sum(result))
