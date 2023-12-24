# problem ......  link = https://codeforces.com/contest/1850/problem/C
# problem Solotion



for _ in range(int(input())):
    test_case = [input().strip() for _ in range(8)]
    Terget = ''
    for i in test_case:
        for j in i:
            if j !='.':

                Terget+=j
    print(Terget)

