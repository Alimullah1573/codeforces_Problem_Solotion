def lucky_ticket(n,tickit):
    if set(tickit)<={'4','7'}:
        first = sum(int(number) for number in tickit[:n//2])
        second = sum(int(number) for number in tickit[n//2:])
        if first == second:
            return 'YES'
    return 'NO'
n = int(input())
tickit = input()
print(lucky_ticket(n,tickit))
