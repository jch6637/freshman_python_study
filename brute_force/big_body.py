n = int(input())
values = []
result = []

for i in range(n):
    tmp = input()
    values.append(tmp.split(' '))

for i in range(n):
    rank = 1
    for j in range(n):
        if int(values[j][0]) > int(values[i][0]) and int(values[j][1]) > int(values[i][1]):
            rank += 1

    result.append(str(rank))

print(' '.join(result))