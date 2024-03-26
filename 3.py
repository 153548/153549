from csv import DictReader, DictWriter
with open('students.csv') as file:
    headers = ['id', 'Name', 'titleProject_id', 'class', 'score']
    data = list(DictReader(file, delimiter = ','))

titleProject_id = input()
while titleProject_id != 'СТОП':
    for student in data:
        if student['titleProject_id'] == titleProject_id:
            (first, second, third) = student['Name'].split()
            print(f'Проект №{student["titleProject_id"]} делал: {second[0]}. {first} он(а) получил(а) оценку - {student["score"]}.')
            break
    else:
        print('Ничего не найдено')

    titleProject_id = input()
