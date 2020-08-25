#Given an array and a number k that's smaller than the length of the array, rotate the array to the right k elements in-place.
a1=[0,1,2,3,4,5,6,7,8,9,10]
k=8
for i in range(k):
	for j in range(len(a1)-1,0,-1):
		a1[j-1],a1[j]=a1[j],a1[j-1]
print(a1)