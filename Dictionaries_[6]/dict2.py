animals = {"Bear": 10, "Horse": 7, "Tigers": 15, "Monkeys": 6}


animals["Zebra"] = 20
print(animals) #{'Bear': 10, 'Horse': 7, 'Tigers': 15, 'Monkeys': 6, 'Zebra': 20}

animals["Bear"] = 12
print(animals) #{'Bear': 12, 'Horse': 7, 'Tigers': 15, 'Monkeys': 6, 'Zebra': 20}

del animals["Horse"]
print(animals) #{'Bear': 12, 'Tigers': 15, 'Monkeys': 6, 'Zebra': 20}