# link : https://codeforces.com/problemset/problem/1896/B

for _ in range(int(input())):
    n = int(input())
    a = str(input())
    ans = len(a) - 1
    for i in range(n):
        if a[i] == 'B':
            ans -= 1
        else:
            break

    for i in range(n - 1, -1, -1):
        if a[i] == 'A':
            ans -= 1
        else:
            break

    if ans >= 0:
        print(ans)
    else:
        print(0)
