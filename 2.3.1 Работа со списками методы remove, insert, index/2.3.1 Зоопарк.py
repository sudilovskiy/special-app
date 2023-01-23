zoo = ['lion', 'kangaruu', 'elephant', 'monkey']

index_lion = zoo.index('lion')

zoo.insert(index_lion + 1, 'bear')
zoo.remove('elephant')
print(f'Зоопарк: {zoo}\n'
      f'Лев сидит в клетке номер {zoo.index("lion")+1}\n'
      f'Обезяна сидит в клетке номер {zoo.index("monkey")+1}')

