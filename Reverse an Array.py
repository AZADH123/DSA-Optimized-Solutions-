"""Problem: Reverse an Array
Reversing an array means rearranging the elements so that the first element becomes the last, the second element becomes the second last, and so on.

Approach: 
Two-Pointer Technique
The two-pointer technique is an efficient way to reverse an array in-place (without using extra space).

Use two pointers:
One pointer (left) starts at the beginning of the array.
The other pointer (right) starts at the end of the array.
Swap the elements at these two pointers.
Move the pointers closer (left++ and right--) until they meet or cross.

Algorithm:
Initialize two pointers: left = 0 and right = n-1 (where n is the size of the array).
While left < right:
Swap arr[left] and arr[right].
Increment left and decrement right.
Stop when left >= right.

Complexity:
Time Complexity: 
O(n), where n is the size of the array. Each element is swapped once.
Space Complexity: 
O(1), as no extra space is used."""

def reverseArray(arr):
    left, right = 0, len(arr) - 1  # Initialize two pointers
    
    while left < right:
        # Swap the elements at left and right
        arr[left], arr[right] = arr[right], arr[left]
        # Move the pointers closer
        left += 1
        right -= 1

    return arr  # The array is reversed in-place

# Example Execution
arr = [1, 2, 3, 4, 5]
reversed_arr = reverseArray(arr)
print("Reversed Array:", reversed_arr)
