text = input("Введите строку: ")
text = list(text)
text_mod = ''
count = 0
for i, letter in enumerate(text):
    if letter == ":":
        letter = ";"
        count += 1
    text_mod += letter

print(f"Исправленная строка: {text_mod}\n"
      f"Количество замен: {count}")
