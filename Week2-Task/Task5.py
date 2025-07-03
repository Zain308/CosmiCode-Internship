def kadanes_algorithm(arr):
    """Find the maximum sum subarray using Kadane's Algorithm."""
    if not arr:
        return 0, []
    
    current_sum = max_sum = arr[0]
    start = temp_start = 0
    end = 0
    
    for i in range(1, len(arr)):
        if arr[i] > current_sum + arr[i]:
            current_sum = arr[i]
            temp_start = i
        else:
            current_sum += arr[i]
        
        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i
    
    return max_sum, arr[start:end+1]

def main():
    try:
        # Get input as a comma-separated list of numbers
        input_str = input("Enter a list of numbers (comma-separated): ")
        arr = [int(x) for x in input_str.split(",")]
        
        if not arr:
            print("The list is empty.")
            return
        
        # Run Kadane's Algorithm
        max_sum, subarray = kadanes_algorithm(arr)
        print(f"Maximum subarray sum: {max_sum}")
        print(f"Subarray with maximum sum: {subarray}")
        
    except ValueError:
        print("Please enter a valid list of integers (e.g., 1, -2, 3).")

if __name__ == "__main__":
    main()