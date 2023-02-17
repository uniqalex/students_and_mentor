class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lector(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in self.courses_in_progress and course in lector.courses_attached:
            if grade in range(1, 10):
                if course in lector.grades:
                    lector.grades[course] += [grade]
                else:
                    lector.grades[course] = [grade]
        else:
            return f'Ошибка! Оцениваемый лектор {lector.name} не закреплен за указанным курсом {course}'

    def abs_grade(self):
        avg_c = []
        for val_list in self.grades.values():
            avg_c += [sum(val_list) / len(val_list)]

        if len(avg_c) == 0:
            return None
        else:
            return round(sum(avg_c) / len(avg_c), 1)

    def __str__(self):
        courses_now = ', '.join(self.courses_in_progress)
        courses_finished = ', '.join(self.finished_courses)
        return f'Имя: {self.name}' \
            + '\n' + f'Фамилия: {self.surname}' \
            + '\n' + f'Средняя оценка за домашние задания: {self.abs_grade()}' \
            + '\n' + f'Курсы в процессе обучения: {courses_now}' \
            + '\n' + f'Завершенные курсы: {courses_finished}'

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Error. You should choose Student')
            return
        else:
            return self.abs_grade() < other.abs_grade()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}


class Lecturer(Mentor):
    def abs_grade(self):
        avg_c = []
        for val_list in self.grades.values():
            avg_c += [sum(val_list) / len(val_list)]
        if len(avg_c) == 0:
            return None
        else:
            return round(sum(avg_c) / len(avg_c), 1)

    def __str__(self):
        return f'Имя: {self.name}' \
            + '\n' + f'Фамилия: {self.surname}' \
            + '\n' + f'Средняя оценка за лекции: {self.abs_grade()}'

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Error. You should choose Lecturer')
            return
        else:
            return self.abs_grade() < other.abs_grade()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}' \
            + '\n' + f'Фамилия: {self.surname}'


#FUNCS
def abs_hworks(stud_list, course):
    hw_list = []
    for s in stud_list:
        if not isinstance(s, Student):
            print('Error. Not a Student')
            return
        else:
            for key, val in s.grades.items():
                if key == course and len(val) != 0:
                    hw_list += [sum(val) / len(val)]
    return round(sum(hw_list) / len(hw_list), 1)


def abs_lections(lector_list, course):
    lection_list = []
    for s in lector_list:
        if not isinstance(s, Lecturer):
            print('Error. Not a Lecturer')
            return
        else:
            for key, val in s.grades.items():
                if key == course and len(val) != 0:
                    lection_list += [sum(val) / len(val)]
    return round(sum(lection_list) / len(lection_list), 1)



#ПОЛЕВЫЕ ИСПЫТАНИЯ
best_student = Student('Ruoy', 'Eman', 'male')
best_student.courses_in_progress += ['Python', 'SQL']

best_student2 = Student('Abu', 'Dabi', 'Unknown')
best_student2.courses_in_progress += ['Python']
best_student2.finished_courses += ['Git', 'SQL']

best_lector = Lecturer('Oleg', 'Buddy')
best_lector.courses_attached += ['Python']

best_lector2 = Lecturer('Ivan', 'Sidorov')
best_lector2.courses_attached += ['Python']

#оценка лекторов
best_student2.rate_lector(best_lector, 'Python', 4)
best_student2.rate_lector(best_lector, 'Python', 1)

best_student2.rate_lector(best_lector2, 'Python', 3)
best_student2.rate_lector(best_lector2, 'Python', 3)

best_student.rate_lector(best_lector2, 'Python', 4)
best_student.rate_lector(best_lector, 'Python', 5)

#оценка студентов
rw = Reviewer(name='Bot', surname='Botovich')
rw.rate_hw(best_student2, 'Python', 4)
rw.rate_hw(best_student, 'Python', 5)
rw.rate_hw(best_student, 'SQL', 5)

print(rw)
print(best_lector)
print(best_student2)
print(best_student2 > best_student)
print(best_lector < best_lector2)

#Test func abs_hworks
stud_l = [best_student, best_student2]
print(best_student, best_student2)
print(abs_hworks(stud_l, 'Python'))

#Test func abs_lections
lect_l = [best_lector, best_lector2]
print(best_lector, best_lector2)
print(abs_lections(lect_l, 'Python'))