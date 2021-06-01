def countConstruct(target, wordBank, memo = None):
	if memo == None: memo = {}

	if target in memo: return memo[target]
	if target == '': return 1

	totalCount = 0
	for word in wordBank:
		if target[:len(word)] == word:	
			suffix = target[len(word):]
			numberofways = countConstruct(suffix, wordBank, memo)
			totalCount += numberofways 

	memo[target] = totalCount
	return totalCount

print(countConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
print(countConstruct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
print(countConstruct('enterapotentot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))
print(countConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', 
	['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee']))