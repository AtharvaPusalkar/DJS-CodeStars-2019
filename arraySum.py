def rangeSum(n, arr, ranges):
    for i in ranges:
        sum = 0
        if i[0] == ' ' and i[1] == ' ':
            for j in arr[:]:
                if j == ' ':
                    continue
                else:
                    sum += int(j)
            return sum
        elif i[0] == ' ':
            for j in arr[:i[1]]:
                if j == ' ':
                    continue
                else:
                    sum += int(j)
        elif i[1] == ' ':
            for j in arr[i[0]:]:
                if j == ' ':
                    continue
                else:
                    sum += int(j)
        else:
            for j in arr[i[0]:i[1]]:
                if j == ' ':
                    continue
                else:
                    sum += int(j)
    return print(sum)

n = int(input())
arr = list(input())
q = int(input())
ranges = []
for j in range(q):
    ranges.append(list(map(int, input().rstrip().split())))
rangeSum(n, arr, ranges)
