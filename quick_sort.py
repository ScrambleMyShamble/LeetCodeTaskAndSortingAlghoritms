# O(nlogn)
def quicksort(array: list) -> list:
    if len(array) < 2:  # Выход из рекурсии, базовый случай
        return array

    else:
        head_element = array[0]  # Выбираем базовый элемент(не важно какой)

        less_part = [i for i in array[1:] if i < head_element]  # здесь все элементы, которые меньше базового
        greater_part = [i for i in array[1:] if i > head_element]  # здесь больше

        return quicksort(less_part) + [head_element] + quicksort(
            greater_part)  # по рекурсии вызываем функцию со списками


list = [56, 36, 75, 48, 98, 76, 90, 71, 1, 4, 54, 6, 86, 5, 9, 45, 11]
print(quicksort(list))
