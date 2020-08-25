def Levenshtein(s1, s2):
	mat = [[0 for x in range(len(s1) + 1)] for y in range(len(s2) + 1)]

	for j in range(len(mat)):
		for i in range(len(mat[j])):
			if (min(i, j) == 0):
				mat[j][i] = max(i, j)
			else:
				mat[j][i] = min(mat[j][i - 1] + 1, 
								mat[j - 1][i] + 1, 
								mat[j - 1][i - 1] + (s2[j - 1] != s1[i - 1]))

	return mat[len(mat) - 1][len(mat[0]) - 1]


data = [
	['Hyundai', 'Honda'],
	['Flomax', 'Volmax'],
	['Gily', 'Geely'],
]

for i in data:
	print(Levenshtein(i[0], i[1]))