class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_details(self):
        print(f"Nom : {self.name}, Age : {self.age}")


class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def display_details(self):
        super().display_details()
        print(f"Salaire : {self.salary}")


john = Person("John", 28)
employee_alice = Employee("Alice", 30, "30 000€")

john.display_details()
employee_alice.display_details()
