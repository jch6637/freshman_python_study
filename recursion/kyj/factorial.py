# factorial

def cal_factorial(N):
    if (N == 0) | (N == 1):
        return 1

    return N * cal_factorial(N-1)

if __name__ == '__main__':
    N = int(input())
    print(cal_factorial(N))