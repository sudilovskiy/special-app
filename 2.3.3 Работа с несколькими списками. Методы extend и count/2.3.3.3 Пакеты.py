amount_packeg = int(input("Количество пактов: "))
result = []
count_error = 0
for i in range(amount_packeg):
    print(f'\nПакет номер {i+1}')
    packeg = []
    for j in range(4):
        packeg.append(int(input(f'{j+1} бит: ')))
    if packeg.count(-1) > 1:
        print("Много ошибок в пакете.")
        count_error += 1
    else:
        result.extend(packeg)

print(f"\nПолученное сообщение: {result}\n"
      f"Количество ошибок в сообщении: {result.count(-1)}\n"
      f"Количество потерянных пакетов: {count_error}")

