class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        avg_grade = sum([sum(grades) / len(grades) for grades in self.grades.values()]) / len(self.grades)
        courses_in_progress_str = ', '.join(self.courses_in_progress)
        finished_courses_str = ', '.join(self.finished_courses)
        return f'Имя: {self.name}\nФамилия: {self.surname}\n' \
               f'Средняя оценка за домашние задания: {avg_grade:.1f}\n' \
               f'Курсы в процессе изучения: {courses_in_progress_str}\n' \
               f'Завершенные курсы: {finished_courses_str}'
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        avg_grade = sum([sum(grades) / len(grades) for grades in self.grades.values()]) / len(self.grades)
        return f'{super().__str__()}\nСредняя оценка за лекции: {avg_grade:.1f}'

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return super().__str__()



student1 = Student('John', 'Doe', 'Male')
student1.courses_in_progress = ['Python']
student1.finished_courses = ['Введение в основы']

student2 = Student('Alice', 'Smith', 'Female')
student2.courses_in_progress = ['Python', 'Git']
student2.finished_courses = ['Введение в основы']

lecturer1 = Lecturer('Bob', 'Johnson')
lecturer1.courses_attached = ['Python']

lecturer2 = Lecturer('Eva', 'White')
lecturer2.courses_attached = ['Git']

reviewer1 = Reviewer('Jack', 'Black')
reviewer1.courses_attached = ['Python']

reviewer2 = Reviewer('Emily', 'Brown')
reviewer2.courses_attached = ['Git']


reviewer1.rate_hw(student1, 'Python', 9)
reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student2, 'Python', 10)
reviewer2.rate_hw(student2, 'Git', 9)

student1.rate_lecture(lecturer1, 'Python', 10)
student2.rate_lecture(lecturer2, 'Git', 9)
student2.rate_lecture(lecturer1, 'Python', 9)
student1.rate_lecture(lecturer2, 'Git', 9)

print(reviewer1)
print(reviewer2)
print(lecturer1)
print(lecturer2)
print(student1)
print(student2)

def avg_grade_by_course_students(students, course):
    grades_sum = sum([sum(student.grades.get(course, [])) for student in students])
    total_grades = sum([len(student.grades.get(course, [])) for student in students])
    return grades_sum / total_grades if total_grades > 0 else 0

def avg_grade_by_course_lecturers(lecturers, course):
    grades_sum = sum([sum(lecturer.grades.get(course, [])) for lecturer in lecturers])
    total_grades = sum([len(lecturer.grades.get(course, [])) for lecturer in lecturers])
    return grades_sum / total_grades if total_grades > 0 else 0


print(f'Средняя оценка за Python у студентов: {avg_grade_by_course_students([student1, student2], "Python"):.1f}')
print(f'Средняя оценка за Python у лекторов: {avg_grade_by_course_lecturers([lecturer1], "Python"):.1f}')
