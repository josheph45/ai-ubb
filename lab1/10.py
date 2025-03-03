# 10. Considerându-se o matrice cu n x m elemente binare (0 sau 1) sortate crescător pe linii,
# să se identifice indexul liniei care conține cele mai multe elemente de 1.
# De ex. în matricea
# [[0,0,0,1,1],
# [0,1,1,1,1],
# [0,0,1,1,1]]
# a doua linie conține cele mai multe elemente 1.

""""""
"""
Time Complexity: O(n * m)
Space Complexity: O(1)
"""
def get_max1_row(matrix):
    num_of_1 = 0
    index = -1
    for row in matrix:
        if row.count(1) > num_of_1:
            num_of_1 = row.count(1)
            index = matrix.index(row)
    return index

def most_1_values(matrix):
    row = max(matrix)
    return matrix.index(row)

X = [[0,0,0,1,1],
    [0,1,1,1,1],
    [0,0,1,1,1]]

print(get_max1_row(X))
print(most_1_values(X))