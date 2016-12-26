def sortStudents(students):
    return list(sorted(students, key=lambda student: (student[0], student[1], student[2])))


students = []
while True:
    ip = input().strip()
    if not ip:
        break
    students.append(tuple(ip.split(',')))

res = sortStudents(students)
print(res)
