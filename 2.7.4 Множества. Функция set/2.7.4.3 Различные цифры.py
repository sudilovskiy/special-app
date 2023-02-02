txt = "ab1n32kz2"

answer = set()
for i in txt:
    if '0' <= i <= '9':
        answer.add(i)
print(" ".join(answer))

