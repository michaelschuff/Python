import time

from random import *


def radixSort(arr):
	if (len(arr) == 0) :
		return []
	maxlen = max(map(lambda x: len(str(x)), arr))
	out = []
	for i in range(len(arr)):
		arr[i] = str(arr[i])
		while (len(arr[i]) < maxlen):
			arr[i] = '0' + arr[i]
		out.append(0)
	counts = []
	for j in range(1, maxlen + 1):
		counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

		for i in range(len(arr)):
			counts[int(arr[i][-j])] += 1
		for i in range(1, len(counts)):
			counts[i] += counts[i-1]

		for i in range(len(arr)-1, -1, -1):
			b = int(str(arr[i])[-j])
			counts[b] -= 1 
			out[int(counts[b])] = arr[i]
		for i in range(len(out)):
			arr[i] = out[i]
			out[i] = 0


	return list(map(lambda x: int(x), arr))

length = 1
maxnum = 1000
data = []
while (length <= 1000000):
	b = []
	for j in range(100):
		a = []
		for i in range(length):
			a.append(randint(0, maxnum))

		start = time.time()
		radixSort(a)
		end = time.time()

		b.append(end - start)
	data.append(sum(b)/len(b))
	length *= 10
print(data)


