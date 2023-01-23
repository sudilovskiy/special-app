name = input("Имя: ")
number_order = input("Номер заказа: ")

msg = "Здравствуйте,{name}! Ваш номер заказа:{number}. Приятного дня!".format(name=name, number=number_order)

print(msg)