# Division 2
# link https://codeforces.com/contest/1946/problem/A

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    ar1 = sorted(arr)
    middel = (n-1)//2
    count = 0
    for i in range(middel,n):
        if ar1[middel] == ar1[i]:
            count +=1
        else:
            break
    print(count)
