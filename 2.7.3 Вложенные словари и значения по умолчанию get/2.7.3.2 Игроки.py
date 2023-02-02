players_dict = {
    1: {'name': 'Vanya', 'team': 'A', 'status': 'Rest'},
    2: {'name': 'Lena', 'team': 'B', 'status': 'Training'},
    3: {'name': 'Maxim', 'team': 'C', 'status': 'Travel'},
    4: {'name': 'Egor', 'team': 'C', 'status': 'Rest'},
    5: {'name': 'Andrei', 'team': 'A', 'status': 'Training'},
    6: {'name': 'Sasha', 'team': 'A', 'status': 'Rest'},
    7: {'name': 'Alina', 'team': 'B', 'status': 'Rest'},
    8: {'name': 'Masha', 'team': 'C', 'status': 'Travel'}
}

count_rest = []
count_training = []
count_travel = []
for number in players_dict.values():
    if number['team'] == 'A' and number['status'] == 'Rest':
        count_rest.append(number['name'])
    elif number['team'] == 'B' and number['status'] == 'Training':
        count_training.append(number['name'])
    elif number['team'] == 'C' and number['status'] == 'Travel':
        count_travel.append(number['name'])

print("Все члены команды А, которые отдыхают {}\n"
      "Все члены команды B, которые тренируются {}\n"
      "Все члены команды C, которые путешествуют{}".
      format(count_rest, count_training, count_travel))
