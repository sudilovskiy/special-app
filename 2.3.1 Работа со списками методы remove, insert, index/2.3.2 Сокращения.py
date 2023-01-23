list_people = [int(input(f'Зарплата {i+1} сотрудника: ')) for i in range(int(input("Количество сотрудников: ")))]
list_people = [i for i in list_people if i != 0]
print(f'\nОсталось сотрудников: {len(list_people)}\n'
      f'Зарплаты: {list_people}\n'
      f'Максимальная зарплата: {max(list_people)}\n'
      f'Минимальная зарплата: {min(list_people)}')