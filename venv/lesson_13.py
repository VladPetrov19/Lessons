
def print_result():
    try:
        a = int(input('A: '))
        b = int(input('B: '))

        print('Result', a/b)
    except ValueError:
        print('Invalid value passed')
    except ZeroDivisionError:
        print('Cannot divide to zero')
    except Exception:
        print('Unknown exception')

print_result()


class TemperatureOverflowError(Exception):
    pass



def control_measurements():
    try:
        # ..... get measurements -> throw ValueError
        pass
    except ValueError:
        raise TemperatureOverflowError

from dataclasses import dataclass

@dataclass
class TVSet:
    diag: int
    colorful: bool
    vendor: str
    matrix: str
    model: str
    # ...

    def turn_on(self):
        pass
    def switch_to_channel(self, number):
        pass


my_tv = TVSet(diag=10, colorful=True, vendor='Sony', matrix='OLED', model='AAA111222y')
my_tv2  = TVSet(diag=10, colorful=False, vendor='Samsung', matrix='OLED', model='AAA114422y')

print(my_tv.model)
print(my_tv2.model)


class Student:

    first_name: str
    last_name: str
    age: int

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ', ' + str(self.age)


s = Student('Ivan', 'Ivanov', 21)

print(s)