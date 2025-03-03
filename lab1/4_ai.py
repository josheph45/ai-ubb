from collections import Counter

"""
Time Complexity: O(n)
Space Complexity: O(n)
"""
def unique_words(text: str) -> list:
    # Find words that appear exactly once in the text
    word_counts = Counter(text.split())
    return [word for word, count in word_counts.items() if count == 1]

text2 = "ana are ana are mere rosii ana"
print(unique_words(text2))  # Output: ['mere', 'rosii']