list_word = ["дождь", "машина", "человек"]
text = "машины едет в дождь а человек в машине сидит"

text = text.split()
answer = [text.count(word) for word in list_word]

print(answer)