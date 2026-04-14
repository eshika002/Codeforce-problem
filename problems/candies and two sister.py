t = int(input())
cases = [int(input()) for _ in range(t)]
results = [(n - 1) // 2 for n in cases]
for res in results:
    print(res)
