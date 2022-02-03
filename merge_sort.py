#O(nlogn)
def merge(array: list):

    length_array = len(array)

    if length_array < 2:    # базовый случай, делим исходный список на равные части пока не дойдем до базового случая
        return array

    left_side = merge(array[:length_array//2])  # левая от начала до середины
    right_side = merge(array[length_array//2:])     # правая от середины до конца

    element_in_the_left = 0     # индексы для сравнения элементов левой части и правой части, элементы левой
    element_in_the_right = 0    # элементы правой части

    result = []
    while element_in_the_left < len(left_side) and element_in_the_right < len(right_side):  # пока не дошли до конца
        # какой либо из частей, сравниваем элементы из разных частей
        if left_side[element_in_the_left] <= right_side[element_in_the_right]: # если в левой части элемент меньше,
            # то добавляем его в результирующий список, и двигаем индекс дальше по левому списку, для сравнения
            result.append(left_side[element_in_the_left])
            element_in_the_left += 1
        else:   # если элемент в правой части меньше, то добавляем его и двигаем индекс дальше по правому
            result.append(right_side[element_in_the_right])
            element_in_the_right += 1

    # на этом этапе у нас сравниваются два отсортированных массива, и если все элементы одного массива добалвены в
    # результирующий то просто добавляем остатки второв массива в конец результирующего
    result += left_side[element_in_the_left:]
    result += right_side[element_in_the_right:]

    return result


list = [56,36,75,48,98,76,90,71,1,4,54,6,86,5,9,45,11]
print(merge(list))

