with open("input.txt") as f:
    lines = f.read().splitlines()

freshIngredientsRanges = []
finalRanges = []
countFreshIngredients = 0

for index, elem in enumerate(lines):
    if elem != '':
        parts = elem.split('-')
        start, end = int(parts[0]), int(parts[1])
        freshIngredientsRanges.append((start, end))
    else:
        break

freshIngredientsRanges.sort()

print(freshIngredientsRanges)


finalRanges.append(freshIngredientsRanges[0])

for interval in freshIngredientsRanges[1:]:
    currentStart, currentEnd = interval
    previousStart, previousEnd = finalRanges[-1]
    # if this holds, it means there is overlap between the intervals
    if currentStart <= previousEnd:
        # choose the most extended end
        finalRanges[-1] = (previousStart, max(currentEnd, previousEnd))
    else: #if no overlap, just add it
        finalRanges.append(interval)

print(finalRanges)

# count how many items are in the non overlaping intervals
for interval in finalRanges:
    start, end = interval
    countFreshIngredients += (end-start+1)
    
print("Number of fresh IDs: ", countFreshIngredients)
