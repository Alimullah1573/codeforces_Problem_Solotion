# Problem Name link     = https://codeforces.com/problemset/problem/233/A
# Solotion

n = int(input())
li = []
if n%2 !=0:
    li.append(-1)
else:
    for i in range(1,n+1):
        if i%2 !=0:
            d = i+1
            li.append(d)
        else:
            d = i-1
            li.append(d)
print(*li)


# 2nd Solotion

N = int(input())
if  N % 2 == 1:
    print(-1)
else:
    permutation = [0] * N
    for i in range(0, N, 2):
        permutation[i] = i + 2
        permutation[i + 1] = i + 1

    print(" ".join(map(str, permutation)))
