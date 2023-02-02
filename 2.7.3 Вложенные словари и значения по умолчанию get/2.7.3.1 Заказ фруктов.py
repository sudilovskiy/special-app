order = {'apple': 2,
         'banana': 3,
         'pear': 1,
         'watermelon': 10,
         'chocolate': 5}

incomes = {
    'apple': 5600.20,
    'orange': 3500.45,
    'banana': 5000.00,
    'bergamot': 3700.56,
    'durian': 5987.23,
    'grapefruit': 300.40,
    'peach': 10000.50,
    'pear': 1020.00,
    'persimmon': 310.00,
}

total_cost = 0
for i in order:
    total_cost += order[i] * incomes.get(i, 0)

print(f"Итоговая стоимость = {total_cost}")
