# Problem link = https://codeforces.com/problemset/problem/228/A


# Solotion

A,B,C,D = list(map(int,input().split()))
All_vale = [A,B,C,D]
Main_value = set(All_vale)
print(len(All_vale)-(len(Main_value)))
