animals = {"Bear": 10, "Horse": 7, "Tigers": 15, "Monkeys": 6}

print(animals.items())

for animal, number in animals.items():
    print("There are {} {} in the zoo".format(number, animal))