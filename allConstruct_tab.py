def allConstruct(target, wordBank):
	arr = [[]] * (len(target) + 1)
	arr[0] = [[]]

	for i in range(len(target) + 1):
		if len(arr[i]) > 0:
			for word in wordBank:
				if target[i : i + len(word)] == word:
					copyArr = [j + [word] for j in arr[i]]
					arr[i + len(word)] = arr[i + len(word)] + copyArr
					
	return arr[len(target)]

print(allConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
print(allConstruct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
print(allConstruct('enterapotentot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))
print(allConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', 
	['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee']))