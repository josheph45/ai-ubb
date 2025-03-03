import math

"""
Time Complexity: O(1)
Space Complexity: O(1) 
"""
def euclidean_distance(point1: tuple, point2: tuple) -> float:
    # Calculate the Euclidean distance between two points
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

point1 = (1, 5)
point2 = (4, 1)
print(euclidean_distance(point1, point2))  # Output: 5.0
