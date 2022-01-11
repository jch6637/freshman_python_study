N, M= input().split()
num_list = input().split()

result = 0
for i in range(int(N)):
    for j in range(i+1, int(N)):
        for k in range(j+1, int(N)):
            sum = int(num_list[i]) + int(num_list[j]) + int(num_list[k])
            #print(sum)
            if sum <= int(M):
                result = max(result, sum)
                
print(result)
