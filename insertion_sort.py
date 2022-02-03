# Худшее O(n2), лучшее O(n)
def insertion_sort(array: list) -> list:

    for i in range(1, len(array)):
        target_element = array[i]   # этот элемент будет сравниваться со всеми остальными, пока не найдётся элемент меньше,
        # как только он найдется мы вставим наш таргет элемент в нужное место
        element_from_sorted_part = i - 1    # первый элемент считаем за часть списка который уже отсортирован

        while element_from_sorted_part >= 0 and array[element_from_sorted_part] > target_element:   # пока мы не дошли до
            # левого края списка(index=0) и пока таргет элемент меньше чем сравниваемый элемент
            array[element_from_sorted_part+1] = array[element_from_sorted_part] # мы делаем замену, замена делается
            # за счет сдвигания больших элементов вправо, чтобы освободить место таргет элементу
            element_from_sorted_part -= 1   # и двигаемся дальше по списку налево

        array[element_from_sorted_part+1] = target_element  # если элемент с которым мы сравниваем наш таргет элемент, меньше
        # то вставляем наш таргет элемент в нужное место, +1 потому что сравниваемый элемент меньше и нам нужно вставить
        # наш таргет элемент ПОСЛЕ сравниваемого

    return array

list = [56,36,75,48,98,76,90,71,1,4,54,6,86,5,9,45,11]
print(insertion_sort(list))