class Student:
    def __init__(self, student_id, name, english_score, c_score, python_score):
        self.student_id = student_id
        self.name = name
        self.english_score = english_score
        self.c_score = c_score
        self.python_score = python_score
        self.total_score = english_score + c_score + python_score
        self.average_score = self.total_score / 3
        self.grade = self.calculate_grade()

    def calculate_grade(self):
        average = self.average_score
        if average >= 90:
            return 'A'
        elif average >= 80:
            return 'B'
        elif average >= 70:
            return 'C'
        elif average >= 60:
            return 'D'
        else:
            return 'F'

class GradeManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student_by_id(self, student_id):
        self.students = [student for student in self.students if student.student_id != student_id]

    def remove_student_by_name(self, name):
        self.students = [student for student in self.students if student.name != name]

    def search_student_by_id(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def search_student_by_name(self, name):
        for student in self.students:
            if student.name == name:
                return student
        return None

    def sort_students_by_total_score(self):
        self.students.sort(key=lambda x: x.total_score, reverse=True)

    def count_students_above_80(self):
        count = sum(1 for student in self.students if student.total_score >= 80)
        return count

    def calculate_ranks(self):
        self.sort_students_by_total_score()
        for i, student in enumerate(self.students):
            student.rank = i + 1

    def display_students(self):
        print("학번\t이름\t영어\tC언어\t파이썬\t총점\t평균\t학점\t등수")
        for student in self.students:
            print(f"{student.student_id}\t{student.name}\t{student.english_score}\t{student.c_score}\t{student.python_score}\t{student.total_score}\t{student.average_score:.2f}\t{student.grade}\t{student.rank}")

def input_student_data():
    manager = GradeManager()
    for _ in range(5):
        student_id = input("학번을 입력하세요: ")
        name = input("이름을 입력하세요: ")
        english_score = int(input("영어 점수를 입력하세요: "))
        c_score = int(input("C언어 점수를 입력하세요: "))
        python_score = int(input("파이썬 점수를 입력하세요: "))
        student = Student(student_id, name, english_score, c_score, python_score)
        manager.add_student(student)
    return manager

def main():
    manager = input_student_data()
    manager.calculate_ranks()
    manager.display_students()
    above_80_count = manager.count_students_above_80()
    print(f"80점 이상 학생 수: {above_80_count}")

    # 추가 기능 테스트
    print("\n--- 추가 기능 테스트 ---")
    print("1. 학생 삽입:")
    new_student = Student("100", "새학생", 85, 75, 90)
    manager.add_student(new_student)
    manager.display_students()

    print("\n2. 학생 삭제(학번):")
    manager.remove_student_by_id("100")
    manager.display_students()

    print("\n3. 학생 삭제(이름):")
    manager.remove_student_by_name("새학생")
    manager.display_students()

    print("\n4. 학번으로 학생 탐색:")
    searched_student = manager.search_student_by_id("10001")
    if searched_student:
        print(f"학번 10001인 학생 정보: {searched_student.name}")
    else:
        print("학번 10001인 학생을 찾을 수 없습니다.")

    print("\n5. 이름으로 학생 탐색:")
    searched_student = manager.search_student_by_name("홍길동")
    if searched_student:
        print(f"이름이 '홍길동'인 학생 정보: {searched_student.student_id}")
    else:
        print("이름이 '홍길동'인 학생을 찾을 수 없습니다.")

    print("\n6. 총점으로 정렬 후 출력:")
    manager.sort_students_by_total_score()
    manager.display_students()

if __name__ == "__main__":
    main()
