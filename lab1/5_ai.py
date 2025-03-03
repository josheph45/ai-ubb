""""""
"""
Time Complexity: O(n)
Space Complexity: O(n)
"""
def find_duplicate(arr: list) -> int:
    # Find the duplicate number in an array with values from {1, 2, ..., n - 1}
    seen = set()
    for num in arr:
        if num in seen:
            return num
        seen.add(num)
    return -1  # Should not happen based on problem constraints

arr = [1, 2, 3, 4, 2]
print(find_duplicate(arr))  # Output: 2