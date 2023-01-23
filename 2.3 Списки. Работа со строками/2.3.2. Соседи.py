text = input("Введите строку: ")
letter_id = int(input("Номер символа: ")) - 1
text = list(text)
print(f"\nСимвол слева: {text[letter_id-1]}")
print(f"Символ справа: {text[letter_id+1]}\n")

if text[letter_id-1] == text[letter_id] and text[letter_id+1] == text[letter_id]:
    print("Есть два таких же")
elif text[letter_id-1] == text[letter_id] or text[letter_id+1] == text[letter_id]:
    print("Есть один такой же")
else:
    print("Одинаковых нет")
