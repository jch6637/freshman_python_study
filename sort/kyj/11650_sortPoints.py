if __name__ == '__main__':
    count = int(input())
    point_l = list()

    for _ in range(0,count):
        point_x, point_y = map(int, input().split())
        point_l.append([point_x, point_y])
    
    point_l.sort()

    for p in point_l:
        print(p[0], p[1])