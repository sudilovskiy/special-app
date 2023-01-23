number_list = []
len_list = int(input("Введите длинну списка: "))

for i in range(len_list):
    number_list.append(int(input(f"Введите {i+1} элемент: ")))

print()
developer = int(input("Введите делитель: "))
print()

count = 0
sum_id = 0
for i in number_list:
    if i % developer == 0:
        print(f"Индекс числа {i}: {count}")
        sum_id += count
    count += 1

print(f"Сумма индексов: {sum_id}")
