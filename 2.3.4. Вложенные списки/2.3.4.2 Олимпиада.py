amaunt = int(input("Введите количество участников: "))
command = int(input("Введите количество человек в команде: "))

answer = []
mini_list = []
for i in range(1, amaunt + 1):
    mini_list.append(i)
    if i % 4 == 0:
        answer.append(mini_list)
        mini_list = []

print(f"\n\nОбщий список команд: {answer}")