""""""
"""
Time Compelxity: O(n)
Space Complexity: O(1)
"""
def sparse_dot_product(vec1: list, vec2: list) -> float:
    # Compute the dot product of two sparse vectors
    return sum(x * y for x, y in zip(vec1, vec2) if x != 0 and y != 0)

vec1 = [1, 0, 2, 0, 3]
vec2 = [1, 2, 0, 3, 1]
print(sparse_dot_product(vec1, vec2))  # Output: 4