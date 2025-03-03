# 6. Pentru un șir cu n numere întregi care conține și duplicate, să se determine elementul majoritar
# (care apare de mai mult de n / 2 ori). De ex. 2 este elementul majoritar în șirul [2,8,7,2,2,5,2,3,1,2,2].

""""""
"""
Time Complexity: O(n^2)
Space Complexity: O(1)
"""
def get_maj_elem(array):
    for el in array:
        if array.count(el) > len(array) / 2:
            return el

print(get_maj_elem([2,8,7,2,2,5,2,3,1,2,2]))