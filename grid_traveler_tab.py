def grid(m, n):
	arr = [[0] * (n + 1) for i in range(m + 1)]
	arr[1][1] = 1

	for i in range(m + 1):
		for j in range(n + 1):
			curr = arr[i][j]
			if (j + 1 <= n): arr[i][j + 1] += curr
			if (i + 1 <= m): arr[i + 1][j] += curr

	return (arr[m][n])

print(grid(2, 2))
print(grid(3, 2))
print(grid(3, 3))
print(grid(100, 10))