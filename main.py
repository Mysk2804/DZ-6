class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def ave_gread(self):
        number = []
        for gre in self.grades.values():
            number.extend(gre)
        if number:
            ave_gre = sum(number) / len(number)
            return ave_gre

    def __lt__(self, other):
        if (not isinstance(self, Student)) or (not isinstance(other, Student)):
            return
        if self.ave_gread() > other.ave_gread():
            print(f'Cредняя оценка за домашнее задание выше у {self.name}')
        else:
            print(f'Cредняя оценка за домашнее задание выше у {other.name}')


    def __str__(self):
        return f'''Имя: {self.name} 
Фамилия: {self.surname}
Средняя оценка за домашние задания: {self.ave_gread()}
Курсы в процессе изучения: {", ".join(self.courses_in_progress)}
Завершенные курсы: {", ".join(self.finished_courses)}'''


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_in_progress = []
        self.grades = {}

    def ave_gread(self):
        number = []
        for gre in self.grades.values():
            number.extend(gre)
        if number:
            ave_gre = sum(number) / len(number)
            return ave_gre

    def __str__(self):
        return f'''Имя: {self.name} 
Фамилия: {self.surname} 
Средняя оценка за лекции: {self.ave_gread()}'''

    def __lt__(self, other):
        if (not isinstance(self, Lecturer)) or (not isinstance(other, Lecturer)):
            return
        if self.ave_gread() > other.ave_gread():
            print(f'Cредняя оценка за лекции выше у {self.name}')
        else:
            print(f'Cредняя оценка за лекции выше у {other.name}')



class Reviewer(Mentor):
    def __str__(self):
        return f'''Имя: {self.name} 
Фамилия: {self.surname}'''

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'




best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Введение в программирование']

super_student = Student('Alexey', 'Popov', 'man')
super_student.courses_in_progress += ['Python']
super_student.courses_in_progress += ['Git']
super_student.finished_courses += ['Введение в программирование']



cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['Git']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Git', 5)

cool_reviewer.rate_hw(super_student, 'Python', 10)
cool_reviewer.rate_hw(super_student, 'Git', 3)

cool_lecturer = Lecturer('Andrey', 'Petrovich')
cool_lecturer.courses_in_progress += ['Python']
cool_lecturer.courses_in_progress += ['Git']

best_lecturer = Lecturer('Voktor', 'Andreich')
best_lecturer.courses_in_progress += ['Python']
best_lecturer.courses_in_progress += ['Git']


best_student.rate_hw(cool_lecturer, 'Python', 2)
best_student.rate_hw(cool_lecturer, 'Git', 2)

best_student.rate_hw(best_lecturer, 'Python', 3)
best_student.rate_hw(best_lecturer, 'Git', 5)



print()
print(super_student)
print()
print(best_student)
print()
print(cool_lecturer)
print()
print(cool_reviewer)
print()
best_student.__lt__(super_student)
print()
it = cool_lecturer >best_lecturer







