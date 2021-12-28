def hanoi(n, start, end, tmp):
    global result

    # 종료
    if n == 1:
        result.append([start, end])
        return

    hanoi(n-1, start, tmp, end)
    result.append([start, end])
    hanoi(n-1, tmp, end, start)

    return

if __name__ == '__main__':
    n = int(input())
    result = list()
    hanoi(n, 1, 3, 2)
    count = len(result)

    print(count)
    for i in result:
        print(i[0], i[1])