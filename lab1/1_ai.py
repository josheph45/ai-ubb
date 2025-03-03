""""""
"""
Time Complexity: O(n)
Space Complexity: O(n)
"""
def last_alphabetical_word(text: str) -> str:
    # Split the text into words and return the max based on lexicographical order
    return max(text.split())

# Example usage
text = "Ana are mere rosii si galbene"
print(last_alphabetical_word(text))  # Output: "si"
