def howSum(targetSum, numbers, memo = None):
	if memo == None: memo = {}

	if targetSum in memo: return memo[targetSum]
	if targetSum == 0: return []
	if targetSum < 0: return None

	for num in numbers:
		rem = targetSum - num
		remResult = howSum(rem, numbers, memo)
		if remResult != None:
			memo[targetSum] = remResult + [num]
			return remResult + [num]

	memo[targetSum] = None
	return None

print(howSum(7, [2, 3]))
print(howSum(7, [5, 3, 4, 7]))
print(howSum(7, [2, 4]))
print(howSum(8, [2, 3, 5]))
print(howSum(300, [7, 14]))