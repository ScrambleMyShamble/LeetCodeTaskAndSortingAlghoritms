class Solution:
    def findLucky(self, arr: List[int]) -> int:
        result = 0
        for i in arr:
            if arr.count(i) == i:
                if i > result:
                    result = i
        if result == 0:
            return -1
        else:
            return result