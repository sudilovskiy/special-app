sample = input("Введите шаблон поздравления который содержит {name} и {age}: ")
peoples = input("Список людей через запятую: ").split(", ")
age = input("Возраст каждого человека через пробел: ").split(" ")

for i in range(len(peoples)):
    print(sample.format(name=peoples[i], age=age[i]))
    birthday_people = " ".join([peoples[i], age[i]])

peoples = [" ".join([peoples[i], age[i]]) for i in range(len(peoples))]

print("Именники:", " ".join(peoples))

