nums = [1, 1, 1, 1, 1]
result = []

for i in nums:
    if nums.count(i) == 1:
        result.append(i)
print(sum(result))
