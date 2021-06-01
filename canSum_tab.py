def canSum(targetSum, numbers):
	arr = [False] * (targetSum + 1)
	arr[0] = True

	for i in range(targetSum + 1):
		if arr[i] == True:
			for num in numbers:
				if (i + num <= targetSum): arr[i + num] = True

	return (arr[targetSum])
	
print(canSum(7, [2, 3]))
print(canSum(7, [5, 3, 4, 7]))
print(canSum(7, [2, 4]))
print(canSum(8, [2, 3, 5]))
print(canSum(300, [7, 14]))