text_user = []
for i in range(3):
    text_user.append(input(f"Введите {i+1} слово: "))
print()
text = []
while True:
    word = input('Слово из текста: ')
    if word == 'end':
        break
    text.append(word)

print("\nПодсчёт слов в тексте")
for word_user in text_user:
    count = 0
    for word_text in text:
        if word_text == word_user:
            count += 1
    print(f"{word_user}: {count}")


