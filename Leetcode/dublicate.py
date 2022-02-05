def func(nums: list):
    first = 0
    second = 1

    while second < len(nums):
        if nums[first] == nums[second]:
            nums.pop(second)
        else:
            first += 1
            second += 1
    return len(nums)


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(func(nums))
