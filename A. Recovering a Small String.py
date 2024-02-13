
#   https://codeforces.com/contest/1931/problem/A

'''def word(encoded_value):
    size = 26
    result = []

    for i in range(1, size + 1):
        for j in range(1, size + 1):
            for k in range(1, size + 1):
                all_sum = i + j + k
                if all_sum == encoded_value:
                    result.append(chr(ord('a') + i - 1) + chr(ord('a') + j - 1) + chr(ord('a') + k - 1))
                    return result
for _ in range(int(input())):

    n = int(input())
    result = word(n)
    print(result[0])
'''