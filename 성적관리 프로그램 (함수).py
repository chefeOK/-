def input_scores():
    student_scores = []
    for i in range(5):
        student = {}
        student['학번'] = input('학번: ')
        student['이름'] = input('이름: ')
        student['영어'] = int(input('영어: '))
        student['C-언어'] = int(input('C-언어: '))
        student['파이썬'] = int(input('파이썬: '))
        student_scores.append(student)
    return student_scores

def calculate_total_average(scores):
    for student in scores:
        student['총점'] = student['영어'] + student['C-언어'] + student['파이썬']
        student['평균'] = student['총점'] / 3

def calculate_grade(scores):
    for student in scores:
        if student['평균'] >= 90:
            student['학점'] = 'A+'
        elif student['평균'] >= 80:
            student['학점'] = 'A'
        elif student['평균'] >= 70:
            student['학점'] = 'B+'
        elif student['평균'] >= 60:
            student['학점'] = 'B'
        else:
            student['학점'] = 'F'

def calculate_rank(scores):
    sorted_scores = sorted(scores, key=lambda x: x['총점'], reverse=True)
    for i, student in enumerate(sorted_scores):
        student['등수'] = i + 1

def print_scores(scores):
    print('성적관리 프로그램')
    print('=' * 85)
    print('학번\t\t이름\t\t영어\tC-언어\t파이썬\t총점\t평균\t학점\t등수')
    print('=' * 85)
    for student in scores:
        print(f"{student['학번']}\t{student['이름']}\t\t{student['영어']}\t{student['C-언어']}\t{student['파이썬']}\t{student['총점']}\t{student['평균']:.2f}\t{student['학점']}\t{student['등수']}")
    print('=' * 85)

scores = input_scores()
calculate_total_average(scores)
calculate_grade(scores)
calculate_rank(scores)
print_scores(scores)