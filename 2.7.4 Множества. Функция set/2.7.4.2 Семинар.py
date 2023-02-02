from random import randint

nums_1 = [randint(1, 30) for _ in range(30)]
nums_2 = [randint(1, 30) for _ in range(30)]
print(nums_1)
print(nums_2)
print()

nums_1 = set(nums_1)
nums_2 = set(nums_2)
print(nums_1)
print(nums_2)
print()

nums_1.remove(min(nums_1))
print(nums_1)
print()

nums_1.add(randint(100, 200))
print(nums_1)
print()

print(nums_1 | nums_2)

print(nums_1 & nums_2)

print(nums_2 - nums_1)