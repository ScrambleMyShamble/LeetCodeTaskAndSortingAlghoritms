# Сложность данного алогритма O(n²), потому что мы проходимся 2 раза по списку
# Первый раз мы идём по списку в основной функции selectionSort
# Второй раз когда отдаём элемент в функцию find_smallest, которая проходится по всему списку,сравнивая принятый элемент

def find_smalles(list): # Эта функция ищет наименьший элемент в списке, и возвращает его индекс
    smallest = list[0] # Хранение наименьшего элемента
    smallest_index = 0 # Хранение индекса наименьшего элемента

    for i in range(1, len(list)):
        if list[i] < smallest:
            smallest = list[i]
            smallest_index = i
    return smallest_index


def selectionSort(list):  # Эта функция создает новый списко куда будут добавляться отсортированный элементы через find_smallest
    sorted_list = []
    for i in range(len(list)): # Проходимся по всему списку
        smallest = find_smalles(list) # Делегируем нахождение наименьшего элемента функции find_smallest
        sorted_list.append(list.pop(smallest)) # Функция find_smallest вернула нам наименьший элемент, удалеяем его из основного списка
    return sorted_list                         # и параллельно добавляем в новый


list = [56,36,75,48,98,76,90,71,1,4,54,6,86,5,9,45,11]
print(selectionSort(list))

# Сортировка выбором без создания второго списка, сортируем сразу исходный список.
for i in range(len(list) - 1):
    smallest_elem_index = i
    next_elem_index = i + 1

    while next_elem_index < len(list):
        if list[next_elem_index] < list[smallest_elem_index]:
            smallest_elem_index = next_elem_index
        next_elem_index += 1
    list[i], list[smallest_elem_index] = list[smallest_elem_index],list[i]