a = int(input("Левая граница: "))
b = int(input("Правая граница: "))

list_square = [i ** 2 for i in range(a, b + 1)]
list_cube = [i ** 3 for i in range(a, b + 1)]

print(f"\nСписок кубов в диапазоне от {a} до {b}: {list_cube}\n"
      f"Список квадратов в диапазоне от {a} до {b}: {list_square})")
