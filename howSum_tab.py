def howSum(targetSum, numbers):
	arr = [None] * (targetSum + 1)
	arr[0] = []

	for i in range(targetSum + 1):
		if arr[i] != None:
			for num in numbers:
				if (i + num <= targetSum): arr[i + num] = arr[i] + [num]

	return arr[targetSum]


print(howSum(7, [2, 3]))
print(howSum(7, [5, 3, 4, 7]))
print(howSum(7, [2, 4]))
print(howSum(8, [2, 3, 5]))
print(howSum(300, [7, 14]))