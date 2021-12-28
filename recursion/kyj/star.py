def print_star(n):
    global star_arr

    # count = 3
    if n == 3:
        star_arr[0][:3] = '***'
        star_arr[1][:3] = '* *'
        star_arr[2][:3] = '***'
        return

    count = n//3
    print_star(count)
    for x in range(3):
        for y in range(3):
            for element in range(count):
                if x == 1 & y ==1:
                    continue
                star_arr[x*count+element][count*y:count*(y+1)] = star_arr[element][:count]

    return


if __name__ == '__main__':
    n = int(input())

    star_arr = [[' ' for i in range(n)] for i in range(n)]

    print_star(n)

    for i in star_arr:
        for j in i:
            print(j, end='')
        print()