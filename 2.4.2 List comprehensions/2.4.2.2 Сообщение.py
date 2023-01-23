msg = input("Введите строку: ")
bonus_lit = input("Дополнительный символ: ")

double_lit = [i * 2 for i  in msg]
gluing_bonus = [i + bonus_lit for i in double_lit]

print(f"\nСписок удвоенных символов: {double_lit}\n"
      f"Склейка с дополнительным символом: {gluing_bonus}")
