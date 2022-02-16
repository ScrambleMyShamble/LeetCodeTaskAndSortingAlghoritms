nums = [5, 1, 5, 2, 5, 3, 5, 4]

rep = len(nums) // 2
set_nums = set(nums)

print(list(el for el in set_nums if nums.count(el) == rep)[0])
