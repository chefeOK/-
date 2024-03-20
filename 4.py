students = []


for i in range(5):
    student = {}
    student['학번'] = input('학번을 입력하세요: ')
    student['이름'] = input('이름을 입력하세요: ')
    student['영어'] = int(input('영어 점수를 입력하세요: '))
    student['C언어'] = int(input('C언어 점수를 입력하세요: '))
    student['파이썬'] = int(input('파이썬 점수를 입력하세요: '))
    students.append(student)


for student in students:
    total = student['영어'] + student['C언어'] + student['파이썬']
    average = total / 3
    student['총점'] = total
    student['평균'] = average

    if average >= 90:
        student['학점'] = 'A'
    elif average >= 80:
        student['학점'] = 'B'
    elif average >= 70:
        student['학점'] = 'C'
    elif average >= 60:
        student['학점'] = 'D'
    else:
        student['학점'] = 'F'


students.sort(key=lambda x: x['총점'], reverse=True)

for i, student in enumerate(students):
    student['등수'] = i + 1


for student in students:
    print('학번:', student['학번'])
    print('이름:', student['이름'])
    print('총점:', student['총점'])
    print('평균:', student['평균'])
    print('학점:', student['학점'])
    print('등수:', student['등수'])
    print()