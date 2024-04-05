
# https://codeforces.com/contest/520/problem/A
n = int(input())
s = str(input()).lower()
d = (set(s))
if len(d)==26:
    print('YES')
else:
    print('NO')

