def brute_force_mario(scores):
    prev = 0
    result = 0

    for i in range(10):
        result += scores[i]

        if result == 100: return 100
        elif result > 100:
            if abs(100 - prev) == abs(100 - result): return max(prev, result)
            if abs(100 - prev) > abs(100 - result): return result
            return prev
        
        prev = result

    return result

scores = []
for i in range(10):
    scores.append(int(input()))

print(brute_force_mario(scores))