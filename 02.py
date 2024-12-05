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
        if value < 0:
            raise ValueError("Опыт работы не может быть отрицательным")
        self._experience = value

    def get_teacher_data(self):
        return f"{self._name}, образование {self._education}, опыт работы {self._experience} года"

    def add_mark(self, student_name, mark):
        return f"{self._name} поставил оценку {mark} студенту {student_name}"

    def remove_mark(self, student_name, mark):
        return f"{self._name} удалил оценку {mark} студенту {student_name}"

    def give_a_consultation(self, student_class):
        return f"{self._name} провел консультацию в классе {student_class}"

class DisciplineTeacher(Teacher):
    def __init__(self, name, education, experience, discipline, job_title):
        super().__init__(name, education, experience)
        self._discipline = discipline
        self.job_title = job_title

    @property
    def discipline(self):
        return self._discipline

    @property
    def job_title(self):
        return self._job_title

    @job_title.setter
    def job_title(self, value):
        self._job_title = value

    def get_teacher_data(self):
        base_data = super().get_teacher_data()
        return f"{base_data}. \nПредмет {self._discipline}, должность {self._job_title}"

    def add_mark(self, student_name, mark):
        base_response = super().add_mark(student_name, mark)
        return f"{base_response}. \nПредмет: {self._discipline}"

    def remove_mark(self, student_name, mark):
        base_response = super().remove_mark(student_name, mark)
        return  f"{base_response}. \nПредмет: {self._discipline}"

    def give_a_consultation(self, student_class):
        base_response = super().give_a_consultation(student_class)
        return f"{base_response}. \nПо предмету {self._discipline} как {self._job_title}"

discipline_teacher = DisciplineTeacher("Иван Петров", "БГПУ", 4, "Химия", "Директор")

print(discipline_teacher.get_teacher_data())
print()
print(discipline_teacher.add_mark("Николай Иванов", 4))
print()
print(discipline_teacher.remove_mark("Дмитрий Сидоров", 3))
print()
print(discipline_teacher.give_a_consultation("10Б"))
