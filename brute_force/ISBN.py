def brute_force_isbn(isbn):
    for i in range(10):
        tmp = isbn.replace('*', str(i))
        total = 0 

        for j in range(12):
            if j % 2 == 0:
                total += int(tmp[j])
            else:
                total += int(tmp[j]) * 3

        if (total + int(tmp[12])) % 10 == 0: return i

isbn = input()
print(brute_force_isbn(isbn))