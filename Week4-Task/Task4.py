def char_frequency(text):
    # Initialize an empty dictionary to store character frequencies
    freq = {}
    
    # Iterate through each character in the input string
    for char in text:
        # Update frequency count in dictionary
        freq[char] = freq.get(char, 0) + 1
    
    return freq

# Example usage
text = "hello world"
result = char_frequency(text)
for char, count in result.items():
    print(f"Character '{char}' appears {count} time(s)")