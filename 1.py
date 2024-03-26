from csv import DictReader, DictWriter
with open('students.csv') as file:
    headers = ['id', 'Name', 'titleProject_id', 'class', 'score']
    data = list(DictReader(file, delimiter = ','))

summ = 0
count = 0
for student in data:
    if student['Name'].startswith('Хадаров Владимир'):
        print(f'Ты получил: {student["score"]}, за проект - {student["titleProject_id"]}')

    if student['score'] != 'None':
        summ += int(student['score'])
        count += 1
average = round(summ/count, 3)
for student in data:
    if student['score'] == 'None':
        student['score'] = average

with open('student_new.csv', 'w') as file:
    writer = DictWriter(file, delimiter = ',', fieldnames = headers)
    writer.writeheader()
    writer.writerows(data)
    

