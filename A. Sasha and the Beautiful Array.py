def max_beauty(t,cases):
    results = []
    for i in cases:
        n = i[0]
        arr = sorted(i[1])
        beauty = sum(arr[k] - arr[k - 1] for k in range(1, n))
        results.append(beauty)
    return results
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    test_cases.append((n, arr))
result = max_beauty(t, test_cases)
for res in result:
    print(res)

