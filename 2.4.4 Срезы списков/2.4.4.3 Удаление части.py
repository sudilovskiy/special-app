from random import randint

work_list = [i for i in range(randint(10, 30))]

a = 0
b = 0
while a >= b:
    a = randint(0, len(work_list))
    b = randint(0, len(work_list))

print(f"list = {work_list}\n"
      f"a = {a}\n"
      f"b = {b}\n")

work_list = work_list[:a] + work_list[b + 1:]
print(f"answer: {work_list}")
