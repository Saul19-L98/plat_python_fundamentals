squares=[x**2 for x in range(1,11)]
print("Squares:",squares)

matrix=[[1,2,3],
        [4,5,6],
        [7,8,9]]
transposed=[[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(matrix)
print(transposed)
