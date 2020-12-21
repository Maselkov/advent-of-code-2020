import puzzleinput

foods = []
for line in puzzleinput.lines:
    ingredients, allergens = line.split(" (contains ")
    allergens = allergens[:-1].split(", ")
    ingredients = ingredients.split()
    print(allergens)
    print(ingredients)
    foods.append((ingredients, allergens))
print(foods)
unique_allergens = set()
unique_ingredients = set()
translations = {}
for food in foods:
    for allergen in food[1]:
        unique_allergens.add(allergen)
    for ingredient in food[0]:
        unique_ingredients.add(ingredient)
all_options = set()
for allergen in unique_allergens:
    options = None
    for food in foods:
        if allergen not in food[1]:
            continue
        if not options:
            options = set(food[0])
        else:
            options &= set(food[0])
    for option in options:
        all_options.add(option)
non_allergenic = unique_ingredients - all_options
print(non_allergenic)
total = 0
for food in foods:
    for ingredient in food[0]:
        if ingredient in non_allergenic:
            total += 1
print(total)
