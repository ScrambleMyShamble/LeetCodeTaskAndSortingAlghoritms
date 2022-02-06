# Задача: найти в списке 2 числа сумма которых равна target
def fun(numbers, target):
    lowest = 0
    highest = len(numbers) - 1
    while lowest < highest:
        result = numbers[lowest] + numbers[highest]  # Весь смысл в том, что идём с 2 концов и проверяем

        if result == target:
            return lowest + 1, highest + 1

        elif result < target:  # если меньше двигаем начало вперед
            lowest += 1

        else:  # если больше, двигаем конец в начало
            highest -= 1


numbers = [2, 9, 7, 11, 15]
target = 9
print(fun(numbers, target))
