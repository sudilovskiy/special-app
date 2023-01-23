price_list = [float(input("Цена на товар: ")) for _ in range(5)]
up_price_1 = int(input("Повышение в первый год: "))
up_price_2 = int(input("Повышение во второй год: "))

answer_1 = sum(price_list)

price_list = [i + i * up_price_1 / 100 for i in price_list]
answer_2 = sum(price_list)
price_list = [i + i * up_price_2 / 100 for i in price_list]
answer_3 = sum(price_list)

print(f"Сумма цен за каждый год: {answer_1}, {answer_2}, {answer_3}")
