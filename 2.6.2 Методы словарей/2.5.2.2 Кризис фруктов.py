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
min_income = min(incomes.values())
income = 0
for i, j in incomes.items():
    income += j
    if min_income == j:
        answer = i
incomes.pop(answer)

print("Общий доход за год составил: {}".format(income))
print(f"Самый маленький доход у {answer}. Он составил {min_income})")

print(f"Итоговый словарь: {incomes}")