import string

def find_longest_word(sentence):
    # Remove punctuation from the sentence
    translator = str.maketrans('', '', string.punctuation)
    clean_sentence = sentence.translate(translator)
    
    # Split the sentence into words
    words = clean_sentence.split()
    
    # If no words are found, return an empty string
    if not words:
        return ""
    
    # Find the longest word
    longest_word = words[0]
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    
    return longest_word

# Test the function
if __name__ == "__main__":
    # Get input from user
    sentence = input("Enter a sentence: ")
    result = find_longest_word(sentence)
    if result:
        print("Longest word:", result)
    else:
        print("No words found in the sentence.")