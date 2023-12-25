# Problem Link   ............ =  https://codeforces.com/problemset/problem/1872/A
# Solotion


import math
for _ in range(int(input())):

    a,b,c = map(int,input().split())
    main = math.ceil((a+b)/2)
    main -= min(a,b)
    main = int(math.ceil(main/c))
    print(main)

