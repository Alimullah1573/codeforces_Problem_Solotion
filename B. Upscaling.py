def solve():
    n = int(input())
    for i in range(n):
        for j in range(n):
            if (i + j) % 2 == 0:
                print("##", end='')
            else:
                print("..", end='')
        print()
        for j in range(n):
            if (i + j) % 2 == 0:
                print("##", end='')
            else:
                print("..", end='')
        print()

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
