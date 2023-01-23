message_1 = input("Первое сообщение: ")
message_2 = input("Второе сообщение: ")

count_symbol_1 = message_1.count("!") + message_1.count("?")
count_symbol_2 = message_2.count("!") + message_2.count("?")

if count_symbol_1 > count_symbol_2:
    print(f'\n Третье сообщение: {message_1} {message_2}')
elif count_symbol_2 > count_symbol_1:
    print(f'\n Третье сообщение: {message_2} {message_1}')
else:
    print("Ой")