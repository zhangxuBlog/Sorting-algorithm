import random

def bubble_sort(l):
	'''
		冒泡排序
		时间复杂度O(n**2)
		稳定
	'''
	for i in range(len(l)):
		for j in range(i + 1, len(l)):
			if l[i] > l[j]:
				l[i], l[j] = l[j], l[i]
	return l

def choice_sort(l):
	'''
		选择排序
		O(n**2)
		不稳定
	'''
	for i in range(len(l)):
		min = i
		for j in range(i + 1, len(l)):
			if l[j] < l[min]:
				min = j
		l[min], l[i] = l[i], l[min]
	return l

def quick_sort(l):
	'''
		快速排序
		O(nlogn)
		不稳定
	'''
	if len(l) < 2:
		return l
	key = l[0]
	l_list = [i for i in l[1:] if i <= key]
	r_list = [i for i in l[1:] if i > key]
	return quick_sort(l_list) + [key] + quick_sort(r_list)

def insert_sort(l):
	'''
		插入排序
		O(n**2)
		稳定
	'''
	for i in range(1, len(l)):
		key = l[i]
		j = i-1
		while j >= 0 and l[j] > l[j + 1]:
			l[j + 1], l[j] = l[j], l[j + 1]
			j -= 1
	return l

def merge_sort(left,right):
	'''
		归并排序
		O(nlongn)
		稳定
	'''
	i = 0
	j = 0
	result = []
	while i < len(left) and j < len(right):
		if left[i] <= right[j]:
			result.append(left[i])
			i += 1
		else:
			result.append(right[j])
			j += 1
	result += left[i:]
	result += right[j:]
	return result

def merge_cut(l):
	#分割为子序列
	if len(l) <= 1:
		return l
	num = len(l)//2	
	left = merge_cut(l[:num])
	right = merge_cut(l[num:])
	return merge_sort(left, right)

def shell_sort(L):
	"""
		希尔排序
		O(n**2)
		不稳定
	"""
	n = len(L)
	gap = n // 2
	while gap > 0:
		for i in range(gap, n):
			while i > 0:
				if L[i - gap] > L[i]:
					L[i], L[i - gap] = L[i - gap], L[i]
					i -= gap
				else:
					break
		gap //= 2
	return L

if __name__ == '__main__':
    L = [x for x in map(lambda x:random.randrange(50), range(10))]
    print('原始列表: ', L)
    print('冒泡排序: ', bubble_sort(L))
    print('插入排序: ', insert_sort(L))
    print('快速排序: ', quick_sort(L))
    print('选择排序: ', choice_sort(L))
    print('希尔排序: ', shell_sort(L))
    print('归并排序: ', merge_cut(L))