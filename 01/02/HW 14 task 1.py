class GroupLimitError(Exception):
    def __init__(self, message="Неможливо додати більше 10 студентів до групи"):
        self.message = message
        super().__init__(self.message)
class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name
    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.age} years old, {self.gender}"
class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book
    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.age} years old, {self.gender}, Record book: {self.record_book}"
class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()
    def add_student(self, student):
        if len(self.group) >= 10:
            raise GroupLimitError()
        self.group.add(student)
    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None
    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)
    def __str__(self):
        all_students = '\n'.join(str(student) for student in self.group)
        return f'Number: {self.number}\nStudents: {len(self.group)}\n{all_students}'



gr = Group('PD1')
for i in range(10):
    student = Student('Male', 20 + i, f'Student{i}', f'Surname{i}', f'AN{i}')
    gr.add_student(student)
    print(f"Додано студента {i + 1}")

print(f"\nУ групі {len(gr.group)} студентів")
print(gr)
print()
try:
    student11 = Student('Female', 22, 'Anna', 'Smith', 'AN11')
    gr.add_student(student11)
    print("Студента додано")
except GroupLimitError as e:
    print(f"Помилка: {e}")

print(f"\nПісля спроби додавання: у групі {len(gr.group)} студентів")