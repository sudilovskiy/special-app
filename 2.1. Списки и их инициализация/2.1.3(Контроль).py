number_of_employees = int(input("Количество сотрудников в офисе: "))
empoloyees_ID = []
for _ in range(number_of_employees):
    new_ID = int(input("ID сотрудника: "))
    empoloyees_ID.append(new_ID)

find_ID = int(input("Какой ID ищем? "))

if find_ID in empoloyees_ID:
    print("Сотрудник на месте.")
else:
    print("Сотрудник не работает!")