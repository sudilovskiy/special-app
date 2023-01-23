a = int(input("Введите число A: "))
b = int(input("Введите число B: "))

answer = [i for i in range(a, b) if i % 2 == 0]

print("Ответ:", answer)