goods = [
    ["яблоки", 50],
    ["апельсины", 190],
    ["груши", 100],
    ["нектарины", 200],
    ["бананы", 77]
]

print(f"Текущий ассортимент: {goods}")

goods.append([input("Новый фрукт: "), int(input("Его цена: "))])
print(f"\nНовый ассортимент: {goods}")

for i in range(len(goods)):
    goods[i][1] = round(goods[i][1]*1.08, 2)

print(f"\nНовый ассортимент  с увеличиной ценой: {goods}")

