for _ in range(int(input())):
    n = input().split(':')
    a = (n[0])
    b = (n[1])
    h = int(a)
    m = int(b)

    if h == 00:
        print(f'{12}:{b} AM')
    elif h<=11:
        print(f'{a}:{b} AM')
    else:
        if h == 12:
            print(f'{a}:{b} PM')
        else:
            d = h-12
            if d>=10:
                print(f'{d}:{b} PM')
            else:
                print(f'0{d}:{b} PM')

