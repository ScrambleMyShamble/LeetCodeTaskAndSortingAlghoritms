heights = [5,1,2,3,4]
sorted_array = sorted(heights)
cnt = 0
index = 0

while len(heights) > index:
    if heights[index] != sorted_array[index]:
        cnt += 1
        index += 1
    else:
        index += 1
print(cnt)
