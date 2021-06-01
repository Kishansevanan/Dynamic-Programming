def countConstruct(target, wordBank):
	arr = [0] * (len(target) + 1)
	arr[0] = 1

	for i in range(len(target) + 1):
		if arr[i] > 0:
			for word in wordBank:
				if target[i:i + len(word)] == word:
					arr[i + len(word)] += arr[i]
		
	return arr[len(target)]


print(countConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
print(countConstruct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
print(countConstruct('enterapotentot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))
print(countConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', 
	['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee']))