from csv import DictReader, DictWriter
with open('students.csv') as file:
    headers = ['id', 'Name', 'titleProject_id', 'class', 'score']
    data = list(DictReader(file, delimiter = ','))

first = {"Name": '', "score": 0}
second = {"Name": '', "score": 0}
third = {"Name": '', "score": 0}
for student in data:
    if student['class'][:2] == '10':
        current_score = int(student['score'])
        second_n, first_n, third_n = student['Name'].split()
        if current_score > first["score"]:
            third['Name'] = second['Name']
            third['score'] = second['score']
            second['Name'] = first['Name']
            second['score'] = first['score']
            first['Name'] = first_n[0] + '.'+' '+ second_n
            first['score'] = current_score
        elif current_score > second['score']:
            third['Name'] = second['Name']
            third['score'] = second['score']
            second['Name'] = first_n[0] + '.'+' '+ second_n
            second['score'] = current_score
        elif current_score > third['score']:
            third['Name'] = first_n[0] + '.'+' '+ second_n
            third['score'] = current_score
print(f'''
10 класс:

1 место: {first['Name']}

2 место: {second['Name']}

3 место: {third['Name']}
''')

