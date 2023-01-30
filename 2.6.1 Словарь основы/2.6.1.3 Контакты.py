contacts = {}
while True:
    print(f"\nТекущие контакты: ")
    for i in contacts:
        print(i, contacts[i])
    name = input("Введите имя: ")
    phone = input("Введите номер телефона: ")
    if name not in contacts:
        contacts[name] = phone
    else:
        print("Ошибка: Такое имя уже существует.")