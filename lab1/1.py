# 1. Să se determine ultimul (din punct de vedere alfabetic) cuvânt care poate apărea
# într-un text care conține mai multe cuvinte separate prin ” ” (spațiu).
# De ex. ultimul (dpdv alfabetic) cuvânt din ”Ana are mere rosii si galbene” este cuvântul "si".

""""""
"""
Time Complexity: O(nlogn)
Space Complexity: O(n)
"""
def get_last_lexico(text):
    words = text.split()
    words.sort()
    return words[-1]

print(get_last_lexico("Ana are mere rosii si galbene"))