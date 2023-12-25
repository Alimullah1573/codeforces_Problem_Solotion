# problem link    =   https://codeforces.com/problemset/problem/231/A
 # Solotion

solotion = 0
for _ in range(int(input())):

    Petya, Vasya, Tonya  = map(int,input().split())
    if (Petya+Vasya+Tonya) == 2 or (Petya+Vasya+Tonya)  == 3:
        solotion +=1
print(solotion)


