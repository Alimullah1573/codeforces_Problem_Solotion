
# Problem link  .....  https://codeforces.com/problemset/problem/118/A

def Solution_string(s):
    all_vowels = set("AEIOUYaeiouy")
    result = []
    for i in s:
        if i not in all_vowels:
            result.append('.')
            result.append(i.lower())

    return ''.join(result)
input_str = input()
result_str = Solution_string(input_str)
print(result_str)
