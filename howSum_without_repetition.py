def howSum(targetSum, numbers, memo = None):
	if memo == None: memo = {}

	if targetSum in memo: return memo[targetSum]
	if targetSum == 0: return []
	if targetSum < 0: return None

	for num in numbers:
		rem = targetSum - num
		newNumbers = numbers[:]
		newNumbers.remove(num)
		remResult = howSum(rem, newNumbers)
		if remResult != None:
			memo[targetSum] = remResult + [num]
			return memo[targetSum]

	memo[targetSum] = None
	return None

print(howSum(7, [2, 3]))
print(howSum(7, [5, 3, 4, 7]))
print(howSum(7, [2, 4, 3]))
print(howSum(8, [2, 3, 5]))
print(howSum(301, [2, 5, 5, 5, 5, 5, 5]))