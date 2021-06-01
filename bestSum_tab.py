def bestSum(targetSum, numbers):
	arr = [None] * (targetSum + 1)
	arr[0] = []

	for i in range(targetSum + 1):
		if arr[i] != None:
			for num in numbers:
				if i + num <= targetSum:
					combination = arr[i] + [num]
					if arr[i + num] == None or len(combination) < len(arr[i + num]):
						arr[i + num] = combination

	return arr[targetSum]



print(bestSum(7, [2, 3]))
print(bestSum(7, [5, 3, 4, 7]))
print(bestSum(7, [2, 4]))
print(bestSum(8, [2, 3, 5]))
print(bestSum(300, [7, 14]))
