def allConstruct(target, wordBank, memo = None):
	if memo == None: memo = {}

	if target in memo: return memo[target]
	if target == '': return [[]]

	totalWays = []

	for word in wordBank:
		if target[:len(word)] == word:
			suffix = target[len(word):]
			suffixWays = allConstruct(suffix, wordBank, memo)
			numberofways = [[word] + suffixWays[i] for i in range(len(suffixWays))]
			totalWays += numberofways
	
	memo[target] = totalWays
	return totalWays

print(allConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
print(allConstruct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
print(allConstruct('enterapotentot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))
print(allConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', 
	['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee']))