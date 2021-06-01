def fib(n):
	arr = [0] * (n + 1)
	arr[1] = 1

	for i in range(n + 1):
		curr = arr[i]
		if (i + 1 <= n): arr[i + 1] += curr
		if (i + 2 <= n): arr[i + 2] += curr

	return arr[n]

print(fib(3))
print(fib(4))
print(fib(5))
print(fib(50))