n = int(input("Введите количество собак: "))

dog_points = []
for i in range(n):
    dog_points.append(int(input(f"Введите количество очков для {i+1} собаки: ")))

min_points = max_point = dog_points[0]
id_dog_min = id_dog_max = 0

for index, i in enumerate(dog_points):
    if i < min_points:
        min_points = i
        id_dog_min = index
    if i > max_point:
        max_point = i
        id_dog_max = index

print(f"Старый список {dog_points}")
dog_points[id_dog_min], dog_points[id_dog_max] = dog_points[id_dog_max], dog_points[id_dog_min]
print(f"Новый список {dog_points}")
