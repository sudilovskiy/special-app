from random import randint

detachment_1 = [randint(50, 80) for _ in range(10)]
detachment_2 = [randint(30, 60) for _ in range(10)]

detachment_3 = [("Погиб " if (detachment_1[i] + detachment_2[i]) > 100
                 else "Выжил")
                for i in range(10)]
print(f"Урон первого отряда: {detachment_1}\n"
      f"Урон второго отряда: {detachment_2}\n"
      f"Состояние третьего отряда: {detachment_3}")
