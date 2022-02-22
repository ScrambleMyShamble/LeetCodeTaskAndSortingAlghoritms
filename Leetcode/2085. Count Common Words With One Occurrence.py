words1 = ["a", "ab"]
words2 = ["a", "a", "a", "ab"]
cnt = 0
for i in words1:
    if words1.count(i) == 1 and words2.count(i) == 1:
        cnt += 1
    else:
        continue

print(cnt)
