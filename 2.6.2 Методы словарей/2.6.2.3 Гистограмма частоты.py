txt = input("Введите текст: ")

answer = dict()

for i in txt:
    if i in answer:
        answer[i] += 1
    else:
        answer[i] = 1

for i, j in answer.items():
    print(f"Символ {i} встречается {j} раз")

print(f"Максимальное количество раз {max(answer.values())}")

