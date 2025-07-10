def is_palindrome(s):
    # Convert to lowercase and remove spaces
    cleaned = s.lower().replace(" ", "")
    
    # Compare the string with its reverse
    left, right = 0, len(cleaned) - 1
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    
    return True

# Test the function
if __name__ == "__main__":
    # Get input from user
    user_input = input("Enter a string: ")
    if is_palindrome(user_input):
        print(f'"{user_input}" is a palindrome.')
    else:
        print(f'"{user_input}" is not a palindrome.')