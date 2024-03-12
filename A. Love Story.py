# link https://codeforces.com/problemset/problem/1829/A

for _ in range(int(input())):
    n = 'codeforces'
    c = 0
    d = str(input())
    for i in range(len(n)):
        if n[i] != d[i]:
            c +=1
    print(c)