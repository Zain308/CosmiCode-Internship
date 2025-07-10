import string

def most_frequent_word(file_path):
    try:
        # Read the file
        with open(file_path, 'r') as file:
            text = file.read()
        
        # Convert to lowercase and remove punctuation
        translator = str.maketrans('', '', string.punctuation)
        clean_text = text.translate(translator).lower()
        
        # Split into words
        words = clean_text.split()
        
        # If no words are found, return None
        if not words:
            return None, 0
        
        # Count word frequencies
        word_count = {}
        for word in words:
            if word:  # Skip empty strings
                word_count[word] = word_count.get(word, 0) + 1
        
        # Find the word with the highest frequency
        max_word = max(word_count, key=word_count.get)
        max_count = word_count[max_word]
        
        return max_word, max_count
    
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None, 0
    except Exception as e:
        print(f"Error: {str(e)}")
        return None, 0

# Test the function
if __name__ == "__main__":
    file_path = input("Enter the path to the text file: ")
    word, count = most_frequent_word(file_path)
    if word:
        print(f"Most frequent word: '{word}' (appears {count} times)")
    else:
        print("No valid words found in the file.")