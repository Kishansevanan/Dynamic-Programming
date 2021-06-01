def grid(m, n, memo = {}):
	if (m, n) in memo: return memo[m, n]
	if (m == 1 and n == 1): return 1
	if (m < 0 or n < 0): return 0

	memo[m, n] = grid(m - 1, n, memo) + grid(m, n - 1, memo)
	return memo[m, n]

print(grid(2, 2))
print(grid(3, 2))
print(grid(2, 3))
print(grid(3, 3))
print(grid(100, 10))
