n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
sum_good_elements = 0
for i in range(n):
    for j in range(n):
        if i == j or i + j == n - 1 or i == n // 2 or j == n // 2:
            sum_good_elements += matrix[i][j]
print(sum_good_elements)