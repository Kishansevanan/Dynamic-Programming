def canConstruct(target, wordBank):
	arr = [False] * (len(target) + 1)
	arr[0] = True

	for i in range(len(target) + 1):
		if arr[i] == True:
			for word in wordBank:
				if target[i:i + len(word)] == word:
					arr[i + len(word)] = True

	return arr[len(target)]


print(canConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
print(canConstruct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
print(canConstruct('enterapotentot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))
print(canConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', 
	['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee']))