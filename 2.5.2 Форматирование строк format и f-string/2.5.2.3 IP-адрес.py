msg_ip = "{0}.{1}.{2}.{3}"

answer = []
for _ in range(4):
    answer.append(int(input(": ")))

print(msg_ip.format(*answer))

