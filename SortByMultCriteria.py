'''
You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string, age
and height are numbers. The tuples are input by console. The sort criteria is:
1: Sort based on name;
2: Then sort based on age;
3: Then sort by score.
The priority is that name > age > score.
'''

import operator


def sortStudents(students):
    return list(sorted(students, key=operator.itemgetter(0, 1, 2)))


'''
def sortStudents(students):
    return list(sorted(students, key=lambda student: (student[0], student[1], student[2])))
'''

students = []
while True:
    ip = input().strip()
    if not ip:
        break
    students.append(tuple(ip.split(',')))

res = sortStudents(students)
print(res)
