#2143

if __name__ == '__main__':
    num = str(input())
    num_list = list(map(str, num))

    num_list.sort(reverse=True)
    for n in num_list:
        print(n, end='')