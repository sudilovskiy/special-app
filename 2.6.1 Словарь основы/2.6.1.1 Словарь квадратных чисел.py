num = int(input("Введите целове число: "))

dic_sqr = {}
for i in range(1, num + 1):
    dic_sqr[i] = i ** 2

print("Результат: {}".format(dic_sqr))