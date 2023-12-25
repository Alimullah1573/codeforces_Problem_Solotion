# Problem link    = https://codeforces.com/problemset/problem/236/A

# Solotion

Girl_Boy = str(input()).lower()
Selected = set(Girl_Boy)
if len(Selected) % 2 == 0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')