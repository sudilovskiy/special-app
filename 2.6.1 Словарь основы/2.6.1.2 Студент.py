info_student = input("Введите информацию о студенте через пробел (имя, фамилия, город, место учёбы, оценки): ")

info_student = info_student.split()
info_student = {
    "name": info_student[0],
    "last_name": info_student[1],
    "city": info_student[2],
    "city_stud": info_student[3],
    "estimates": info_student[4:],
}

for i in info_student:
    print(f"{i} - {info_student[i]}\n")
