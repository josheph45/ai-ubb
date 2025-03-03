# 5. Pentru un șir cu n elemente care conține valori din mulțimea {1, 2, ..., n - 1}
# astfel încât o singură valoare se repetă de două ori, să se identifice acea valoare care se repetă.
# De ex. în șirul [1,2,3,4,2] valoarea 2 apare de două ori.

""""""
"""
Time Complexity: O(n^2)
Space Complexity: O(1)
"""
def get_repeating(array):
    for el in array:
        if array.count(el) > 1:
            return el

print(get_repeating([1,2,3,4,2]))