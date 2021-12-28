def hanoi(n, start, end, aux):
    global result
    if n == 1:
        result.append([start, end])
        return

    hanoi(n - 1, start, aux, end)
    result.append([start, end])
    hanoi(n - 1, aux, end, start)

n = int(input())

global result
result = []
hanoi(n, 1, 3, 2)

print(len(result))
for stage in result:
    print(stage[0], stage[1])