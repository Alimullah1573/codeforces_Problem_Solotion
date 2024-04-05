for _ in range(int(input())):
    n = int(input())
    s = 0
    arr = list(map(int,input().split()))
    for i in arr:
        s+=abs(i)
    print(s)

