if __name__ == '__main__':
    count = int(input())
    word_l = list()

    for _ in range(0,count):
        word_l.append(str(input()))
    
    word_l = list(set(word_l))
    word_l.sort()
    word_l.sort(key=len)

    for p in word_l:
        print(p)