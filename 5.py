from csv import DictReader, DictWriter

with open('students.csv') as file:
    headers = ['id', 'Name', 'titleProject_id', 'class', 'score']
    data = list(DictReader(file, delimiter=','))

m = 10 ** 9 + 9


def get_hash(name):
    s = name.split()
    s1 = s[0] + s[1] + s[2]
    p = 67
    hash = 0
    for i in range(len(s1)):
        t = ord(s1[i]) * p ** i
        hash += t

    hash = hash % m
    return hash


for student in data:
    student['id'] = get_hash(student['Name'])

with open('students_with_hash.csv', 'w') as file:
    writer = DictWriter(file, delimiter=',', fieldnames=headers)
    writer.writeheader()
    writer.writerows(data)

