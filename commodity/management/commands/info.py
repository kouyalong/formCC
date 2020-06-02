# coding: utf-8


def quick_sort(array):
	if len(array) < 1:
		return array
	mid = array(len(array) // 2)
	r = [a for a in array if a > mid]
	l = [a for a in array if a < mid]
	mid = []
	return quick_sort(l) + mid + quick_sort(r)


aaa = quick_sort([1, 4, 5, 3, 6])
print(aaa)

