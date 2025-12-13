with open("input.txt") as f:
    lines = f.read().splitlines()

# store fresh ingredient ranges
freshIngredientsRanges = []
countFreshIngredients = 0

for index, elem in enumerate(lines):
    if elem != '':
        parts = elem.split('-')
        start, end = int(parts[0]), int(parts[1])
        freshIngredientsRanges.append((start, end))    
    else:
        startIngredientList = index+1
        break
    
def isInRanges(num, ranges):
    # any returns true if any value in the iterable returns true
    return any(start <= num <= end for start, end in ranges)

for ingredient in lines[startIngredientList:]:
    ingredientId = int(ingredient)
    if isInRanges(ingredientId, freshIngredientsRanges):
        countFreshIngredients += 1

print("Fresh ingredient count:", countFreshIngredients)
