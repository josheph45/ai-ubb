"""
Time Complexity: O(n log n)
Space Complexity: O(n)
"""
def binary_numbers_upto_n(n: int) -> list:
    # Generate all binary numbers from 1 to n
    return [bin(i)[2:] for i in range(1, n + 1)]

n = 4
print(binary_numbers_upto_n(n))  # Output: ['1', '10', '11', '100']