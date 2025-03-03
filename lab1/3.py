# 3. Să se determine produsul scalar a doi vectori rari care conțin numere reale.
# Un vector este rar atunci când conține multe elemente nule. Vectorii pot avea oricâte dimensiuni.
# De ex. produsul scalar a 2 vectori unisimensionali [1,0,2,0,3] și [1,2,0,3,1] este 4.

""""""
"""
Time Complexity: O(n)
Space Complexity: O(1)
"""
def scalar_product(vect1, vect2):
    sum = float(0)
    for i in range (len(vect1)):
        sum += vect1[i]*vect2[i]
    return sum

print(scalar_product([1,0,2,0,3], [1,2,0,3,1]))