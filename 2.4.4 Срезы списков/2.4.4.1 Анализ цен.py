from random import randint

original_prices = [randint(-100, 100) for _ in range(randint(0, 20))]

new_prices = [0 if i < 0 else i for i in original_prices]

print("Мы потеряли: ",  sum(original_prices) - sum(new_prices))