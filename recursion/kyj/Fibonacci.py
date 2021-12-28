# Fibonacci

def cal_fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return cal_fibo(n-1) + cal_fibo(n-2)

if __name__ == '__main__':
    #n = int(input())
    n = 17
    print(cal_fibo(n))