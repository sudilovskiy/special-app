films = [

    'Крепкий орешек', 'Назад в будущее', 'Таксист',

    'Леон', 'Богемская рапсодия', 'Город грехов',

    'Мементо', 'Отступники', 'Деревня',

    'Проклятый остров', 'Начало', 'Матрица'

]

my_film = []
while True:
    print(f"Ваш текущий топ фильмов: {my_film}")
    film = input("Название фильма: ")
    print("Команды: добавить, вставить, удалить")
    action = input("Введите команду: ")
    match action:
        case 'добавить':
            if film in films:
                my_film.append(film)
            else:
                print("Такого фильма у нас нет.")
        case 'вставить':
            my_film.insert(int(input("Введите позицию: "))-1, film)
        case 'удалить':
            if film in my_film:
                my_film.remove(film)
            else:
                print('Такого фильма у вас в коллекции нет.')
