def reverse_list(arr):
    # Get the length of the list
    length = 0
    for _ in arr:
        length += 1
    
    # Create a new list to store reversed elements
    reversed_arr = [0] * length
    
    # Fill the new list in reverse order
    for i in range(length):
        reversed_arr[i] = arr[length - 1 - i]
    
    return reversed_arr

# Test the reverse function
if __name__ == "__main__":
    # Sample list
    original_list = [1, 2, 3, 4, 5]
    print("Original list:", original_list)
    reversed_list = reverse_list(original_list)
    print("Reversed list:", reversed_list)