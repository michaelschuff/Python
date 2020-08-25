#Let X be a set of n intervals on the real line. We say that a set of points P "stabs" X if every interval in X contains at least one point in P. Compute the smallest set of points that stabs X.

#For example, given the intervals [(1, 4), (4, 5), (7, 9), (9, 12)], you should return [4, 9].

def overlapping(x,y,first):
	if(x[0]<x[1]<y[0]<y[1]):
		return([])
	if(x[0]<x[1]==y[0]<y[1]):
		return([x[1]])
	if(x[0]<y[0]<x[1]<y[1]):
		return([y[0],x[1]])
	if(x[0]<y[0]<x[1]==y[1]):
		return([y[0],x[1]])
	if(x[0]<y[0]<y[1]==x[1]):
		return([y[0],y[1]])
	if(first):
		return(overlapping(y,x,False))
	return([])

X=[[1, 4], [4, 5], [7, 9], [9, 12]
poi=[[]]
for a in range(len(X)):
	for b in range(a+1,len(x)):
		poi.append(overlapping(X[a],X[b],True))
print(poi)