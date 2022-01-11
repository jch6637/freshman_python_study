num = str(input())
num_list = list(map(str, num))
num_len = len(num_list)

sum = 0
star_weight = 1
for idx, item in enumerate(num_list):
    if item != '*': 
        if idx%2:
            sum+=int(item)*3 
        else:
            sum+=int(item)
    elif idx%2: star_weight = 3

for i in range(10):
    if (sum + (i * star_weight)) % 10 == 0:
        print(i)