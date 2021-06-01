def howSum(targetSum, numbers):
	arr = [None] * (targetSum + 1)
	arr[0] = []

	i = 0
	while(True):
		if arr[i] != None:
			for num in numbers:
				if (i + num <= targetSum): 
					arr[i + num] = arr[i] + [num]
					newNumbers = numbers[:]
					newNumbers.remove(num)
					while(len(newNumbers) > 0):
						for n in newNumbers:
							if (num + n <= targetSum): 
								arr[i + n] = arr[i] + [n]
							newNumbers.remove(n)
					if arr[targetSum] != None:
						return arr[targetSum]
					arr = [None] * (targetSum + 1)
					arr[0] = []

	return arr[targetSum]

print(howSum(7, [2, 3]))
print(howSum(7, [5, 3, 4, 7]))
print(howSum(7, [2, 4]))
print(howSum(8, [2, 3, 5]))
print(howSum(300, [7, 14]))