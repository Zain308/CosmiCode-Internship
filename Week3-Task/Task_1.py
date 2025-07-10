def merge_sort(arr):
    # Base case: if list has 1 or fewer elements, it's already sorted
    if len(arr) <= 1:
        return arr
    
    # Find the middle point to divide the list into two halves
    mid = len(arr) // 2
    
    # Recursively sort the two halves
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    # Merge the sorted halves
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    # Compare elements from both lists and merge in sorted order
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Add remaining elements from left, if any
    result.extend(left[i:])
    # Add remaining elements from right, if any
    result.extend(right[j:])
    
    return result

# Test the merge sort function
if __name__ == "__main__":
    # Sample list of integers
    numbers = [64, 34, 25, 12, 22, 11, 90]
    print("Original list:", numbers)
    sorted_list = merge_sort(numbers)
    print("Sorted list:", sorted_list)