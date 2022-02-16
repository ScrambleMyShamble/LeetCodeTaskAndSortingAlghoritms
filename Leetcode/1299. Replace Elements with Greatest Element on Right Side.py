arr = [400]
cnt = 1

for i in arr[cnt::]:
    if len(arr[cnt::]) == 1:
        print(arr[-1])
        print(-1)
        break
    print(max(arr[cnt::]))
    cnt += 1
