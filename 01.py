class Teacher:
    def __init__(self, name, education, experience):
        self._name = name
        self._education = education
        self._experience = experience

    @property
    def name(self):
        return self._name

    @property
    def education(self):
        return self._education

    @property
    def experience(self):
        return self._experience

    @experience.setter
    def experience(self, value):
        self._experience = value

    def get_teacher_data(self):
        return f"{self._name}, образование {self._education}, опыт работы {self._experience} года."

    def add_mark(self, student_name, mark):
        return f"{self._name} поставил оценку {mark} студенту {student_name}."

    def remove_mark(self, student_name, mark):
        return f"{self._name} удалил оценку {mark} студенту {student_name}."

    def give_a_consultation(self, student_class):
        return f"{self._name} провел консультацию в классе {student_class}."

teacher = Teacher("Иван Петров", "БГПУ", 4)

print(teacher.get_teacher_data())
print()
print(teacher.add_mark("Петр Сидоров", 4))
print()
print(teacher.remove_mark("Дмитрий Степанов", 3))
print()
print(teacher.give_a_consultation("9Б"))
