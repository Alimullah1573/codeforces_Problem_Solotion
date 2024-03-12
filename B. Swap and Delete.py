

# link   https://codeforces.com/problemset/problem/1913/B

for  _ in range(int(input())):
    n = str(input())
    one = n.count('1')
    zero = n.count('0')
    for i in range(len(n)):
        if n[i] == '1':
            if (zero>0):
                zero -=1
            else:
                break
        else:
            if one>0:
                one -=1
            else:
                break
    print(one+zero)







