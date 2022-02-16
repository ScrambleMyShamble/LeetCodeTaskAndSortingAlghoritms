nums = [1, 4, 3, 2]
result = 0
for i in range(0, len(nums), 2):
    nums.sort()
    result += min(nums[i:i + 2])

print(result)
