# Problem link  .....   = https://codeforces.com/contest/1873/problem/C
# Solotion

def calculate_points(grid):
    points = 0
    ring_values = [1, 2, 3, 4, 5]

    for i in range(10):
        for j in range(10):
            if grid[i][j] == 'X':
                distance_to_center = min(i, 9 - i, j, 9 - j)
                points += ring_values[distance_to_center]

    return points

def reslt():
    for _ in range(int(input())):
        test_case = [input().strip() for _ in range(10)]
        result = calculate_points(test_case)
        print(result)
if __name__ == "__main__":
    reslt()

