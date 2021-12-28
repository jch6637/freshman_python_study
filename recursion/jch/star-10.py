def generate_default_star():
    top    = '***' + '\n'
    middle = '* *' + '\n'
    bottom = '***' + '\n'

    return [top, middle, bottom]

def star(n):
    if n == 3: return generate_default_star()
    pattern = star(int(n / 3)) # 각 패턴은 상단과 중단, 하단 배열을 반환
    new_top = ''
    new_middle = ''
    
    # 패턴의 상단을 생성
    tmp_top = ''
    tmp_middle = ''
    tmp_bottom = ''
    for _ in pattern[0].split('\n')[:-1]:
        tmp_top += _ * 3 + '\n' 

    for _ in pattern[1].split('\n')[:-1]:
        tmp_middle += _ * 3 + '\n'

    for _ in pattern[2].split('\n')[:-1]:
        tmp_bottom += _ * 3 + '\n'

    new_top = tmp_top + tmp_middle + tmp_bottom

    # 패턴의 중단을 생성
    tmp_top = ''
    tmp_middle = ''
    tmp_bottom = ''
    for _ in pattern[0].split('\n')[:-1]:
        tmp_top += _  + ' ' * len(_) + _ + '\n'

    for _ in pattern[1].split('\n')[:-1]:
        tmp_middle += _  + ' ' * len(_) + _ + '\n'

    for _ in pattern[2].split('\n')[:-1]:
        tmp_bottom += _  + ' ' * len(_) + _ + '\n'

    new_middle = tmp_top + tmp_middle + tmp_bottom

    return [new_top, new_middle, new_top]   # 상단과 하단은 같음

n = int(input())
result = star(n)
print(result[0] + result[1] + result[2], end='')