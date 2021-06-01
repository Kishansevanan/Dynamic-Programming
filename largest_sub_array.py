def largest_sub_array(numbers):
	arr = []

	for num in numbers:
		a = []
		a.append(num)
		index = numbers.index(num)
		for n in numbers[index + 1 :]:
			if n >= num:
				a.append(n)
				num = n
		arr.append(a)

	return max(arr, key = len)

print(largest_sub_array([1, 3, 2, 4, 5]))
print(largest_sub_array([2, 1, 3, 0, 5]))
print(largest_sub_array([1, 1, 1, 1, 1]))
print(largest_sub_array([5, 1, 7, 6, 8]))