

def greeting(name, surname, msg='Hello'):

    print(f'{msg}, {name}, {surname}')

    #return name, surname
#my_c = greeting('name', 'sur')


my_creds = ['Ivan', 'Ivanov']
my_creds_dict = {
    'name': 'Ivan',
    'surname': 'Ivanov'
}

greeting('Ivan', 'Ivanov')
greeting(*my_creds)

greeting(name='Ivan', surname='Ivanov')
greeting(msg='Hi', **my_creds_dict)

a = 1
b = 2

a, b = b, a
# a, b = *(b, a)
c = (b, a)
a, b = c


def foo():
    return 0, 'Hello'


def bar(fn):
    num, _ = fn()
    print(num)

############################
x = 1


def wrapper():

    x = 3
    def myfoo():
        global x
        print(x)

    myfoo()

wrapper()


def increase_number(num):
    return num+100500


def divide_number(num):
    return num/2

numbers = [1, 2, 3, 4]


print(
    list(
        map(
            divide_number,
            map(
                increase_number, numbers
            )
        )
    )
)


def filter_number(num):
    return num % 2 == 0

print(
    list(
        filter(
            filter_number,
            numbers

        )
    )
)

# Список
def range_number(num):
    return num % 3 == 0 or num % 5 == 0

range_numbers = list(range(1,1001))


print(
    list(
        filter(
            range_number,
            range_numbers
        )
    )
)

# Квадраты списка
def range_number(num):
    return num % 3 == 0 or num % 5 == 0

range_numbers = list(range(1,1001))
next_range_numbers = []

for number in range_numbers:
    next_range_numbers.append(number**2)

print(
    list(
        filter(
            range_number,
            next_range_numbers
        )
    )
)







