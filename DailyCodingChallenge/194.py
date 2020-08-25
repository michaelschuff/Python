#Suppose you are given two lists of n points, one list p1, p2, ..., pn on the line y = 0 and the other list q1, q2, ..., qn on the line y = 1. Imagine a set of n line segments connecting each point pi to qi. Write an algorithm to determine how many pairs of the line segments intersect.
y1=[1,2,3,4,5,6,7,8,9,10]
y0=[2,1,4,3,6,5,8,7,10,9]
num=1
for a in range(len(y1)):
	for b in range(len(y0)):
		if(((y1[a]>y1[b] and y0[a]<y0[b]) or (y1[a]<y1[b] and y0[a]>y0[b])) and a!=b):
			num+=1
print(num/2)