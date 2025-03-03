# 2. Să se determine distanța Euclideană între două locații identificate prin perechi de numere.
# De ex. distanța între (1,5) și (4,1) este 5.0

import math

"""
Time Complexity: O(1)
Space Complexity: O(1) 
"""
def euclidean_dist(point1, point2):
    return math.dist(point1, point2)

print(euclidean_dist([1,5], [4,1]))