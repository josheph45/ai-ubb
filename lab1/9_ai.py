""""""
"""
Time Complexity: O(k * n * m) (where k is the number of queries)
Space Complexity: O(k)
"""
def submatrix_sum(matrix: list, queries: list) -> list:
    # Compute sum of elements in submatrices identified by given queries
    results = []
    for (p, q), (r, s) in queries:
        total = sum(matrix[i][j] for i in range(p, r + 1) for j in range(q, s + 1))
        results.append(total)
    return results

matrix = [
    [0, 2, 5, 4, 1],
    [4, 8, 2, 3, 7],
    [6, 3, 4, 6, 2],
    [7, 3, 1, 8, 3],
    [1, 5, 7, 9, 4]
]
queries = [((1, 1), (3, 3)), ((2, 2), (4, 4))]
print(submatrix_sum(matrix, queries))  # Output: [38, 44]