import puzzleinput

foods = []
for line in puzzleinput.lines:
    ingredients, allergens = line.split(" (contains ")
    allergens = allergens[:-1].split(", ")
    ingredients = ingredients.split()
    foods.append((ingredients, allergens))
unique_allergens = set()
unique_ingredients = set()
translations = {}
for food in foods:
    for allergen in food[1]:
        unique_allergens.add(allergen)
    for ingredient in food[0]:
        unique_ingredients.add(ingredient)
allergens = {}
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
    allergens[allergen] = options
non_allergenic = unique_ingredients - all_options
while True:
    for allergen in allergens:
        allergens[allergen] -= non_allergenic
        if len(allergens[allergen]) == 1:
            word = allergens[allergen].copy()
            for allergen_2 in allergens:
                allergens[allergen_2] -= word
            translations[allergen] = word.pop()
    for options in allergens.values():
        if len(options) > 1:
            break
    else:
        break
    continue

tuples = [(k, v) for k, v in translations.items()]
tuples = sorted(tuples, key=lambda t: t[0])
result = ",".join(v for _, v in tuples)
print(result)
