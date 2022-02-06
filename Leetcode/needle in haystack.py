# Дано. Найти вхождение подстроки в строку, вывести индекс первого вхождения

class Solution(object):
    def strStr(self, haystack, needle):

        if needle not in haystack:
            return -1
        if len(needle) == 0:
            return 0
        return haystack.index(needle)
