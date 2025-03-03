# 4. Să se determine cuvintele unui text care apar exact o singură dată în acel text.
# De ex. cuvintele care apar o singură dată în ”ana are ana are mere rosii ana" sunt: 'mere' și 'rosii'.

from collections import Counter

"""
Time Complexity: O(n)
Space Complexity: O(n)
"""
def get_unique_words(text):
    words = text.split()
    words_freq = Counter(words)
    for word in words_freq:
        if words_freq[word] == 1:
            print(word)

get_unique_words("ana are ana are mere rosii ana")