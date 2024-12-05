"""Kadane's Algorithm:
Kadane's Algorithm is a famous approach used to solve the Maximum Subarray Sum problem efficiently in O(n) time. It works by maintaining a running sum of the maximum subarray ending at the current position and updating the global maximum whenever a larger sum is found."""
def maxSubArray(nums):
    # Initialize the variables with the first element
    max_current = max_global = nums[0]
    
    # Loop through the array starting from the second element
    for i in range(1, len(nums)):
        # Update the current maximum subarray sum
        max_current = max(nums[i], max_current + nums[i])
        
        # Update the global maximum if the current is larger
        max_global = max(max_global, max_current)
    
    return max_global

# Example usage:
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSubArray(nums))  # Output: 6