#Задача: перевести римское числов в обычное
romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
cnt = 0
result = 0
s = "MCMXCIV"
while len(s) > cnt + 1:
    if romans[s[cnt]] < romans[s[cnt + 1]]:
        result += (romans[s[cnt + 1]] - romans[s[cnt]])
        cnt += 2
    else:
        result += romans[s[cnt]]
        cnt += 1
if cnt == len(s):
    print(result)
else:
    result += romans[s[len(s) - 1]]
    print(result)
