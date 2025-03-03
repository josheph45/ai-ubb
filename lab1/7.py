# 7. Să se determine al k-lea cel mai mare element al unui șir de numere cu n elemente (k < n).
# De ex. al 2-lea cel mai mare element din șirul [7,4,6,3,9,1] este 7.

""""""
"""
Time Complexity: O(n log n)
Space Complexity: O(n)
"""
def get_k_max(array, k):
    unique = list(set(array))
    unique.sort(reverse=True)
    return unique[k-1]

print(get_k_max([7,4,6,3,9,1],2))