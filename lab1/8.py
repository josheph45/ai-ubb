# 8. Să se genereze toate numerele (în reprezentare binară) cuprinse între 1 și n.
# De ex. dacă n = 4, numerele sunt: 1, 10, 11, 100.

""""""
"""
Time Complexity: O(n log n)
Space Complexity: O(1)
"""
def get_all_bin(n):
    for i in range(1, n+1):
        print(bin(i)[2:])

get_all_bin(4)