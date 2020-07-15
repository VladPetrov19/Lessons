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