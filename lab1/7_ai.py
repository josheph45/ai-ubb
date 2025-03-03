import heapq

"""
Time Complexity: O(n log k)
Space Complexity: O(k)
"""
def kth_largest_element(arr: list, k: int) -> int:
    # Find the k-th largest element in the array
    return heapq.nlargest(k, arr)[-1]

arr3 = [7, 4, 6, 3, 9, 1]
k = 2
print(kth_largest_element(arr3, k))  # Output: 7