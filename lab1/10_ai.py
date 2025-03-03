""""""
"""
Time Complexity: O(n * m) (worst case)
Space Complexity: O(1)
"""
def row_with_most_ones(matrix: list) -> int:
    # Identify the index of the row with the most ones (binary matrix sorted row-wise)
    max_ones = -1
    max_row = -1
    for i, row in enumerate(matrix):
        ones_count = len(row) - row.index(1) if 1 in row else 0
        if ones_count > max_ones:
            max_ones = ones_count
            max_row = i
    return max_row

binary_matrix = [
    [0, 0, 0, 1, 1],
    [0, 1, 1, 1, 1],
    [0, 0, 1, 1, 1]
]
print(row_with_most_ones(binary_matrix))  # Output: 1