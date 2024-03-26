from csv import DictReader, DictWriter
import string
import random
with open('students.csv') as file:
    headers = ['id', 'Name', 'titleProject_id', 'class', 'score', 'login', 'password']
    data = list(DictReader(file, delimiter = ','))

for student in data:
    name = student['Name'].split()
    login = name[0] + '_' + name[1][0] + name[2][0]
    student['login'] = login
    alphabet = string.ascii_letters + string.digits
    password = ''
    nums_check = False
    words_check = False
    while not(words_check and nums_check):
        password = ''
        nums_check = False
        words_check = False
        for i in range(8):
            cur_sym = random.randint(0, 61)
            password += alphabet[cur_sym]
            if alphabet[cur_sym] in string.digits:
                nums_check = True
            elif alphabet[cur_sym] in string.ascii_letters:
                words_check = True
    student['password'] = password

with open('students_password.csv', 'w') as file:
    writer = DictWriter(file, delimiter=',', fieldnames=headers)
    writer.writeheader()

    writer.writerows(data)

