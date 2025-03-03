# 9. Considerându-se o matrice cu n x m elemente întregi și o listă cu perechi formate din coordonatele a 2 căsuțe
# din matrice ((p,q) și (r,s)), să se calculeze suma elementelor din sub-matricile identificate de fieare pereche.
# De ex, pt matricea
# [[0, 2, 5, 4, 1],
# [4, 8, 2, 3, 7],
# [6, 3, 4, 6, 2],
# [7, 3, 1, 8, 3],
# [1, 5, 7, 9, 4]]
# și lista de perechi
# ((1, 1) și (3, 3)), ((2, 2) și (4, 4)),
# suma elementelor din prima sub-matrice este 38,
# iar suma elementelor din a 2-a sub-matrice este 44.

""""""
"""
Time Complexity: O(k * n * m) (where k is the number of pairs)
Space Complexity: O(1)
"""
def get_sum_sub_matrix(matrix, pairs_list):
    for pair in pairs_list:
        sum = 0
        for i in range(pair[0][0], pair[1][0]+1):
            for j in range(pair[0][1], pair[1][1]+1):
                sum += matrix[i][j]
        print(pair, ":", sum)

X = [[0, 2, 5, 4, 1],
    [4, 8, 2, 3, 7],
    [6, 3, 4, 6, 2],
    [7, 3, 1, 8, 3],
    [1, 5, 7, 9, 4]]
pairs = [((1, 1), (3, 3)), ((2, 2), (4, 4))]
get_sum_sub_matrix(X, pairs)