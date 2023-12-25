# Problem link :   = https://codeforces.com/problemset/problem/1/A

# Solotion

m,n,a = map(int,input().split())
area = ((m+(a-1))//a)
lange = ((n+(a-1))//a)
print(area*lange)