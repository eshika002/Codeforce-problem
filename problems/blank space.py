t = int(input())  
results = []      
for _ in range(t):
    n = int(input())  
    arr = list(map(int, input().split()))
    max_blank = 0
    current = 0
    for val in arr:
        if val == 0:
            current += 1
            max_blank = max(max_blank, current)
        else:
            current = 0
    results.append(max_blank)
for ans in results:
    print(ans)
