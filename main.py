
class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_grades = float()
    # Функция заполняющая завершенные курсы у студента
    def add_finished_corsess(self, course_name):
        self.finished_courses.append(course_name)
    # Функция по оценке лекций преподавателя
    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    # Функция для рассчета средней оценки за домашнюю работу у студента
    def calculation_average_grades_homework(student, course):
        if isinstance(student, Student) and course in student.courses_in_progress and student.grades.get(course):
            result = round(float(sum(student.grades.get(course)) / len(student.grades.get(course))) ,2)
            student.average_grades = result
            student.average_course = course
        else:
            return 'Ошибка'
    # Перегрузка
    def __str__(self):
        result = f"Имя: {self.name}\nФамилия: {self.surname}\n" \
                 f"Средняя оценка за домашние задания: {self.average_grades}\n" \
                 f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n" \
                 f"Завершенные курсы: {','.join(self.finished_courses)}"
        return result
    # Проверка сравнения студентов
    def __lt__(self, other):
        if not isinstance(other, Student) or other.average_grades == 0:
            return f'Второй участник сравнения не является студентом курса {self.average_course} или еще не был оценен проверяющим'
        return self.average_grades < other.average_grades
    def __gt__(self, other):
        if not isinstance(other, Student) or other.average_grades == 0:
            return f'Второй участник сравнения не является студентом курса {self.average_course} или еще не был оценен проверяющим'
        return self.average_grades > other.average_grades
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.average_grades = float()
        # Функция подсчета средней оценки лекторов за курс
    def calculation_average_grades_lecture(lecturer, course):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and lecturer.grades.get(course):
            result = round(float(sum(lecturer.grades.get(course)) / len(lecturer.grades.get(course))) ,2)
            lecturer.average_grades = result
            lecturer.average_course = course
        else:
            return 'Ошибка'
    # Перегрузка
    def __str__(self):
        result = f'Имя: {self.name}\nФамилия: {self.surname}\n' \
                 f'Средняя оценка за лекции: {self.average_grades}'
        return result
    # Проверка сравнения лекторов
    def __lt__(self, other):
        if not isinstance(other, Lecturer) or other.average_grades == 0:
            return f'Второй участник сравнения не является лектором курса {self.average_course} или еще не был оценен студентами'
        return self.average_grades < other.average_grades
    def __gt__(self, other):
        if not isinstance(other, Lecturer) or other.average_grades == 0:
            return f'Второй участник сравнения не является лектором курса {self.average_course} или еще не был оценен студентами'
        return self.average_grades > other.average_grades
# Ментор с функией оценки студента
class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    # Перегрузка
    def __str__(self):
        result = f'Имя: {self.name}\nФамилия: {self.surname}'
        return result

# Создаем экземпляры класса Student
student_1 = Student('Виктор', 'Черепахин')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['JAVA']
student_2 = Student('Валерий', 'Гришин')
student_2.courses_in_progress += ['Python']
student_2.courses_in_progress += ['GIT']
student_2.courses_in_progress += ['JAVA']

# Создаем экземпляры класса Lecturer
lecturer_1 = Lecturer('Илья', 'Вещающий')
lecturer_1.courses_attached += ['Python']
lecturer_1.courses_attached += ['JAVA']
lecturer_2 = Lecturer('Анна', 'Красноречивая')
lecturer_2.courses_attached += ['Python']
lecturer_2.courses_attached += ['GIT']

# Создаем экземпляры класса Reviewer
reviewer_1 = Reviewer('Иван', 'Проверяющий')
reviewer_1.courses_attached += ['Python']
reviewer_1.courses_attached += ['JAVA']
reviewer_2 = Reviewer('Николай', 'Всевидящий')
reviewer_2.courses_attached += ['Python']
reviewer_2.courses_attached += ['GIT']
reviewer_2.courses_attached += ['JAVA']

# Добавляем оценки студентам за разные курсы
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_2.rate_hw(student_1, 'Python', 10)
reviewer_2.rate_hw(student_1, 'Python', 10)
reviewer_2.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_2, 'Python', 1)
reviewer_1.rate_hw(student_2, 'Python', 2)
reviewer_1.rate_hw(student_2, 'Python', 3)
reviewer_2.rate_hw(student_2, 'Python', 4)
reviewer_2.rate_hw(student_2, 'Python', 5)
reviewer_2.rate_hw(student_2, 'Python', 6)
reviewer_1.rate_hw(student_1, 'JAVA', 7)
reviewer_1.rate_hw(student_1, 'JAVA', 2)
reviewer_1.rate_hw(student_1, 'JAVA', 1)
reviewer_2.rate_hw(student_1, 'JAVA', 10)
reviewer_2.rate_hw(student_1, 'JAVA', 10)
reviewer_2.rate_hw(student_1, 'JAVA', 10)

# Добавляем оценки лекторам за курс Python
student_1.rate_lecture(lecturer_1, 'Python', 8)
student_1.rate_lecture(lecturer_1, 'Python', 8)
student_1.rate_lecture(lecturer_1, 'Python', 8)
student_2.rate_lecture(lecturer_1, 'Python', 6)
student_2.rate_lecture(lecturer_1, 'Python', 6)
student_2.rate_lecture(lecturer_1, 'Python', 6)
student_1.rate_lecture(lecturer_2, 'Python', 5)
student_1.rate_lecture(lecturer_2, 'Python', 5)
student_1.rate_lecture(lecturer_2, 'Python', 5)
student_2.rate_lecture(lecturer_2, 'Python', 6)
student_2.rate_lecture(lecturer_2, 'Python', 6)
student_2.rate_lecture(lecturer_2, 'Python', 6)

# Добавляем пройденный курс студенту
student_1.add_finished_corsess('Введение в программирование')
student_2.add_finished_corsess('C++')

# Рассчитываем средние оценки для сутеднтов за курс Python
Student.calculation_average_grades_homework(student_1, 'Python')
Student.calculation_average_grades_homework(student_2, 'Python')

# Рассчитываем средние оценки для лекторов за курс Python
Lecturer.calculation_average_grades_lecture(lecturer_1, 'Python')
Lecturer.calculation_average_grades_lecture(lecturer_2, 'Python')

# Проверяем переопределенные методы для созданных классов
print(reviewer_1, end='\n\n')
print(lecturer_1, end='\n\n')
print(lecturer_2, end='\n\n')
# Сравнение лекторов
print(lecturer_1 < lecturer_2, end='\n\n')
# Вывод студентов
print(student_1, end='\n\n')
print(student_2, end='\n\n')
# Сравнение студентов
print(student_1 < student_2, end='\n\n')