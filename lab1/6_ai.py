from collections import Counter

"""
Time Complexity: O(n)
Space Complexity: O(n)
"""
def majority_element(arr: list) -> int:
    # Find the majority element that appears more than n/2 times
    count = Counter(arr)
    n = len(arr)
    for num, freq in count.items():
        if freq > n // 2:
            return num
    return -1  # No majority element found

arr2 = [2, 8, 7, 2, 2, 5, 2, 3, 1, 2, 2]
print(majority_element(arr2))  # Output: 2