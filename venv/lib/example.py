
class Student:

    Dog: str
    last_name: str
    age: int

    def __init__(self, dog, last_name, age):
        self.dog = dog
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return self.dog + ' ' + self.last_name + ', ' + str(self.age)


s = Student('Ivan', 'Ivanov', 21)

print(s)